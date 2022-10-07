# This application uses Flask to fulfill Google Dialogflow requests
# and relay these to GPT API. Following the Friend Chat example to Simulate
# talking to an old friend. With each utterance the entire converstaion is passed
# back and forth between Digalogflow and GPT using an output context called "converstation".

import openai
from flask import Flask
from dialogflow_fulfillment import WebhookClient
from dialogflow_fulfillment import Context

app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/')
def hello():
    return '{"Hello": "World!"}'

#Put your OpenAI key in the config.json file.
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/webhook', methods=['POST','GET']) 
def friend():
      # Handle the incoming request
    body = request.json
    agent = WebhookClient(body)
    query=agent.query
    contexts =Context(agent.context,agent.session)
    context = (contexts.get('converstation'))
    converstation="\n\n"
    if "parameters" in context: #If not first exchange then capture converstation history from context.
        converstation = context['parameters']['converstation'] + "\n\n"

    response = openai.Completion.create( # Build the GPT query.
    engine="text-davinci-001",
    prompt=converstation + " You:" + query,
    temperature=0.5,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    stop=["You:"]
     )
    
    GPTresponse=response["choices"][0]["text"]
    #Capture the entire converstation history and send it as an outputContext
    #that can be feed back into GPT as the prompt as converstation evolves.
    history = {  
        "converstation":converstation + " You:" + query + " " +GPTresponse
        }
    contexts.set('converstation',5,history) 
    agent.add(GPTresponse)
    return agent.response 
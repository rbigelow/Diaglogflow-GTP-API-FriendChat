# Diaglogflow-GTP-API-FriendChat
 
This is a demo Flask application that can be used to connect to the Open AI friend chat API. Using Google Dialogflow as a front end. 

To set this up doe the following
1) get an API key from OpenAI and put it into the config.py file. 
2) Upload this app to a cloud service such as Heroku. 
3) Go to https://dialogflow.cloud.google.com and create an agent. 
4) Click on fulfillment in Dialog flow and set the webhook url to the URL of your cloud app http://MYAPP.HEROKU.COM/friend
5) Go to the default welcome intent and "enable fulfillment. 
6) Enjoy your new AI friend. 


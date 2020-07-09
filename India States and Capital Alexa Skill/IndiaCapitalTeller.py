def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest" :
        return onLaunch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest" :
        return onIntent(event, event['session'])
    elif event['request']['type'] == "SessionEndedRequest" :
        return onSessionEnd(event['request'], event['session'])

def onLaunch(launchRequest, session):
    return welcomeuser()
    
def welcomeuser():
    sessionAttributes = {}
    cardTitle = " Hello! Namaste!"
    speechOutput =  "Hello, Welcome to INDIAN STATES & CAPITALS.\n" \
                    "Today, I will let you know about Indian States and their Capitals." \
                    "You can ask me question by saying 'What is the capital of state called'. " \
                    "Which Indian State's Capital you want to know ?"
    repromptText =  "You can say, for example, 'What is the capital of Punjab called'. "
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def buildResponse(sessionAttr , speechlet):
    return {
        'version': '1.0',
        'sessionAttributes': sessionAttr,
        'response': speechlet
    }

def buildSpeechletResponse(title, output, repromptTxt, endSession):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
            },
            
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
            },
            
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': repromptTxt
                }
            },
        'shouldEndSession': endSession
    }
    
def onSessionEnd(sessionEndedRequest, session):
    print("on_session_ended requestId=" + sessionEndedRequest['requestId'] + ", sessionId=" + session['sessionId'])

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using INDIAN STATES & CAPITALS. " \
                    "Have a great day! "
    shouldEndSession = True
    return buildResponse({}, buildSpeechletResponse(cardTitle, speechOutput, None, shouldEndSession))

  
def onIntent(event, session):
    intent = event['request']['intent']
    intentName = event['request']['intent']['name']
    if intentName == "askState":
        return capitalOfStates(event, session)
    elif intentName == "AMAZON.HelpIntent":
        return welcomeuser()
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handleSessionEndRequest()
    else:
        raise ValueError("Invalid intent")


def capitalOfStates(event, session):
    cardTitle = event['request']['intent']['name']
    sessionAttributes = {}
    shouldEndSession = False
    speechOutput = ''
    if 'value' not in event['request']['intent']['slots']['statename'] :
        speechOutput = "I'm not sure which state you are saying. " \
                       "Please provide a valid Indian State name or say stop to exit. " 
        repromptText = "I'm not sure which state you are saying. " \
                       "Please provide a valid Indian State name or say stop to exit. " 
    
    
    elif event['request']['intent']['slots']['statename']['name'] == 'statename' :
        sname = event['request']['intent']['slots']['statename']['value']
        res=state_dict.get(sname,"")
        speechOutput = "A group of " + sname + " is called " + res +". " \
                       "You can ask me another animal's group name or say stop to close Animal Groups."
        repromptText = "You can ask me another animal's group name or say stop to close Animal Groups."
        if len(res) == 0 :
            speechOutput = "I'm not sure which state you are saying. " \
                       "Please provide a valid Indian State name or say stop to exit. " 
            repromptText = "I'm not sure which state you are saying. " \
                       "Please provide a valid Indian State name or say stop to exit. " 
    else:
         speechOutput ="I'm not sure which state you are saying. " \
                       "Please provide a valid Indian State name or say stop to exit. " 
         repromptText = "I'm not sure which state you are saying. " \
                       "Please provide a valid Indian State name or say stop to exit. " 
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

state_dict={
    "Andhra Pradesh":"Hyderabad",
    "Arunachal Pradesh":"Itanagar",
    "Assam":"Dispur",
    "Bihar":"Patna",
    "Chhattisgarh":"Raipur",
    "Goa":"Panaji",
    "Gujarat":"Gandhinagar",
    "Haryana":"Chandigarh",
    "Himachal Pradesh":"Shimla",
    "Jammu and Kashmir":"Srinagar (in summer), Jammu (in winter)",
    "Jharkhand":"Ranchi",
    "Karnataka":"Bangalore",
    "Kerala":"Thiruvananthapuram",
    "Madhya Pradesh":"Bhopal",
    "Maharashtra":"Mumbai",
    "Manipur":"	Imphal",
    "Meghalaya":"Shillong",
    "Mizoram":"Aizawl",
    "Nagaland":"Kohima",
    "Orissa":"Bhubaneswar",
    "Punjab":"Chandigarh",
    "Rajasthan":"Jaipur",
    "Sikkim":"Gangtok",
    "Tamil Nadu":"Chennai",
    "Telangana":"Hyderabad",
    "Tripura":"Agartala",
    "Uttar Pradesh":"Lucknow",
    "Uttarakhand":"Dehradun",
    "West Bengal":"Kolkata",
    "Andaman and Nicobar":"Port Blair",
    "Chandigarh":"Chandigarh",
    "Dadar and Nagar Haveli":"Silvassa",
    "Daman and Diu":"Daman",
    "Delhi":"New Delhi",
    "Lakshadweep":"Kavaratti",
    "Pondicherry":"Pondicherry"
}
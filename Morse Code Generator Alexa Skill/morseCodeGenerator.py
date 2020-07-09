def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest" :
        return onLaunch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest" :
        return onIntent(event, event['session'])
    elif event['request']['type'] == "SessionEndedRequest" :
        return onSessionEnd(event['request'], event['session'])

def onLaunch(launchRequest, session):
    return welcomeuser()

def onIntent(event, session):
    intent = event['request']['intent']
    intentName = event['request']['intent']['name']
    if intentName == "morse_main":
        return morse_func(event, session)
    elif intentName == "AMAZON.HelpIntent":
        return welcomeuser()
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handleSessionEndRequest()
    else:
        raise ValueError("Invalid intent")

def onSessionEnd(sessionEndedRequest, session):
    print("on_session_ended requestId=" + sessionEndedRequest['requestId'] + ", sessionId=" + session['sessionId'])
   
def welcomeuser():
    sessionAttributes = {}
    cardTitle = "MORSE CODE GENERATOR !!!"
    speechOutput =  "Hello , Welcome to MORSE CODE GENERATOR.\n" \
                    "You can tell me your message to encrypt.\n" \
                    "You can tell your message by saying 'translate message'."
    repromptText =  "Sorry, I'm not sure what you are saying. Please tell me your message again. "
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
    
def handleSessionEndRequest():
    cardTitle = "Session Ended !!!"
    speechOutput = "Thank you for using MORSE CODE GENERATOR. " \
                    "Have a awesome day! "
    shouldEndSession = True
    return buildResponse({}, buildSpeechletResponse(cardTitle, speechOutput, None, shouldEndSession))

def avoids(word, forbidden):
       for letter in word:
              if letter in forbidden:
                     return False
       return True

def morse_func(event, session):
    cardTitle = event['request']['intent']['name']
    sessionAttributes = {}
    shouldEndSession = False
    speechOutput = ''
    input_string=event['request']['intent']['slots']['message']['value']
    input_string=input_string.upper()
    forbidden="{}()[]"
    if avoids(input_string,forbidden) and len(input_string)>0:
        res=[]
        for ch in input_string:
            res.append(morse_dict.get(ch,"#"))
        encrypt_str=" ".join(str(x) for x in res)
        speechOutput = "Your encrypted message for '" + input_string +"' is [ " +encrypt_str +" ]. " \
                    "Please tell me your message or say stop to close MORSE CODE GENERATOR. "
                
        repromptText =  "Please tell me your message or say stop to close MORSE CODE GENERATOR. "
        if len(encrypt_str) == 0 :
            speechOutput = "Please tell me your message or say stop to close MORSE CODE GENERATOR. "
            repromptText =  "Please tell me your message or say stop to close MORSE CODE GENERATOR. "
    else:
            speechOutput = "Your input contains some inalid characters.\nPlease tell me your message or say stop to close MORSE CODE GENERATOR. "
            repromptText =  "Please tell me your message or say stop to close MORSE CODE GENERATOR. "
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))
        

morse_dict={
              "A":"DOT-DASH ",
              "B":"DASH-DOT-DOT-DOT ",
              "C":"DASH-DOT-DASH-DOT ",
              "D":"DASH-DOT-DOT ",
              "E":"DOT ",
              "F":"DOT-DOT-DASH-DOT ",
              "G":"DASH-DASH-DOT ",
              "H":"DOT-DOT-DOT-DOT ",
              "I":"DOT-DOT ",
              "J":"DOT-DASH-DASH-DASH ",
              "K":"DASH-DOT-DASH ",
              "L":"DOT-DASH-DOT-DOT ",
              "M":"DASH-DASH ",
              "N":"DASH-DOT ",
              "O":"DASH-DASH-DASH ",
              "P":"DOT-DASH-DASH-DOT ",
              "Q":"DASH-DASH-DOT-DASH ",
              "R":"DOT-DASH-DOT ",
              "S":"DOT-DOT-DOT ",
              "T":"DASH ",
              "U":"DOT-DOT-DASH ",
              "V":"DOT-DOT-DOT-DASH ",
              "W":"DOT-DASH-DASH ",
              "X":"DASH-DOT-DOT-DASH ",
              "Y":"DASH-DOT-DASH-DASH ",
              "Z":"DASH-DASH-DOT-DOT ",
              "0":"DASH-DASH-DASH-DASH-DASH ",
              "1":"DOT-DASH-DASH-DASH-DASH ",
              "2":"DOT-DOT-DASH-DASH-DASH ",
              "3":"DOT-DOT-DOT-DASH-DASH ",
              "4":"DOT-DOT-DOT-DOT-DASH ",
              "5":"DOT-DOT-DOT-DOT-DOT ",
              "6":"DASH-DOT-DOT-DOT-DOT ",
              "7":"DASH-DASH-DOT-DOT-DOT ",
              "8":"DASH-DASH-DASH-DOT-DOT ",
              "9":"DASH-DASH-DASH-DASH-DOT ",
              "&":"DOT-DASH-DOT-DOT-DOT ",
              "'":"DOT-DASH-DASH-DASH-DASH-DOT ",
              "@":"DOT-DASH-DASH-DOT-DASH-DOT ",
              ":":"DASH-DASH-DASH-DOT-DOT-DOT ",
              ",":"DASH-DASH-DOT-DOT-DASH-DASH ",
              "=":"DASH-DOT-DOT-DOT-DASH ",
              "!":"DASH-DOT-DASH-DOT-DASH-DASH ",
              ".":"DOT-DASH-DOT-DASH-DOT-DASH ",
              "-":"DASH-DOT-DOT-DOT-DOT-DASH ",
              "+":"DOT-DASH-DOT-DASH-DOT ",
              "?":"DOT-DOT-DASH-DASH-DOT-DOT ",
              "/":"DASH-DOT-DOT-DASH-DOT ",
              '"':"DOT-DASH-DOT-DOT-DASH-DOT ",
              " ":" "
       }
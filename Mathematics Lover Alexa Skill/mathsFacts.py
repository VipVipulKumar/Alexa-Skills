def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest" :
        return onLaunch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest" :
        return onIntent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest" :
        return onSessionEnd(event['request'], event['session'])

def onLaunch(launchRequest, session):
    return welcomeuser()

def onIntent(intentRequest, session):
    intent = intentRequest['intent']
    intentName = intentRequest['intent']['name']
    if intentName == "mathsIntent":
        return factsFunction(intent, session)
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
    cardTitle = " Hello, Namaste!!!"
    speechOutput =  "Hello , Welcome to MATHEMATICS FACTS! " \
                    "You can know interesting facts about MATHEMATICS by saying 'tell me facts about mathematics'."
    repromptText =  "You can know interesting facts about MATHEMATICS by saying 'tell me facts about mathematics'."
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def factsFunction(intent, session):
    import random
    index = random.randint(0,len(Facts)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "Learn about MATHEMATICS. An interesting MATHEMATICS FACT :: " + Facts[index] 
    repromptText = "You can know interesting facts about MATHEMATICS by saying 'tell me facts about mathematics'"
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using MATHEMATICS FACTS Alexa Skills Kit. " \
                    "Have a great time! "
    shouldEndSession = True
    return buildResponse({}, buildSpeechletResponse(cardTitle, speechOutput, None, shouldEndSession))

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


def buildResponse(sessionAttr , speechlet):
    return {
        'version': '1.0',
        'sessionAttributes': sessionAttr,
        'response': speechlet
    }


Facts = [
        "A French word for pie chart is 'camembert'.",
        "The spiral shapes of sunflowers follow a Fibonacci sequence.",
        "Zero is the only number that can't be represented in Roman numerals.",
        "The most popular favourite number is 7.",
        "The number 4 is considered unlucky in much of Asia.",
        "The word 'hundred' comes from the old Norse term,'hundrath', which actually means 120 and not 100.",
        "'Forty' is the only number that is spelt with letters arranged in alphabetical order.",
        "'One' is the only number that is spelt with letters arranged in descending order.",
        "From 0 to 1000, the only number that has the letter 'a' in it is 'one thousand'.",
        "‘Four’ is the only number in the English language that is spelt with the same number of letters as the number itself.",
        "Every odd number has an 'e' in it.",
        "'Eleven plus two' is an anagram of 'twelve plus one' which is pretty fitting as the answer to both equations is 13.",
        "The symbol for division is called an obelus.",
        "2 and 5 are the only prime numbers that end in 2 or 5.",
        "A ‘jiffy’ is an actual unit of time. It means 1/100th of a second.",
        "Zero is the only number with most number of the names. Zero is also called naught, nil, zilch, naught and zip.",
        "Name ‘Google’ was actually derived from a misspelt word ‘googol’. Googol practically means 1 followed by 100 zeroes.",
        "Any two opposite sides of a dice, when added make ‘7’.",
        "PI never repeats and never ends when written in decimal numbers. It is irrational."
    ]
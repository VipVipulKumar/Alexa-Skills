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
    if intentName == "humanBodyIntent":
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
    speechOutput =  "Hello , Welcome to HUMAN BODY FACTS! " \
                    "You can know interesting facts about HUMAN BODY by saying 'tell me facts about human body'"
    repromptText =  "You can know interesting facts about HUMAN BODY by saying 'tell me facts about human body'"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def factsFunction(intent, session):
    import random
    index = random.randint(0,len(Facts)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "Learn about HUMAN BODY. An interesting HUMAN BODY FACT :: " + Facts[index] 
    repromptText = "You can know interesting facts about HUMAN BODY by saying 'tell me facts about human body'"
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using HUMAN BODY FACTS Alexa Skills Kit. " \
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


Facts= [
              "Earwax production is necessary for good ear health.",
              "The inner ear is the main organ of balance.",
              "A human ear contains about 24,000 fibers in it.",
              "It only takes 7 pounds of pressure to rip your ear off.",
              "The human ear can distinguish between hundreds of thousands of different sounds.",
              "The human ears can hear in the frequency of 1,000 to 50,000 hertz.",
              "Your ears never stop hearing, even when you sleep. Your brain just ignores incoming sounds.",
              "Tiny hair cells in your inner ear are what translates sound waves to electricity to send to the brain.",
              "After eating too much, your hearing is less sharp.",
              "Your nose can remember 50,000 different scents.",
              "Our nose is our personal air-conditioning system: it warms cold air, cools hot air and filters impurities.",
              "The nerve cells present in the nose, allows us to smell and regenerates through out ones life.",
              "Your eyes are always the same size from birth but your nose and ears never stop growing.",
              "Children have better sense of smell than adults.",
              "You breathe in about 7 quarts of air every minute.",
              "Women have better sense of smell than men.",
              "You have no sense of smell when you're sleeping.",
              "You burn more calories while sleeping than you do when watching television.",
              "The three things pregnant women dream most of during their first trimester are frogs, worms and potted plants.",
              "Scientists say the higher your I.Q. the more you dream.",
              "The human body releases growth hormones during sleep.",
              "Your teeth start growing 6 months before you are born.",
              "The Romans used to clean and whiten their teeth with urine.",
              "Human teeth are almost as hard as rocks.",
              "Plaque begins to form 6 hours after brushing our teeth.",
              "80% of the brain is water.",
              "Any damage to brain cells cannot be repaired completely.",
              "The base of the spinal cord has a cluster of nerves, which are most sensitive.",
              "The Human brain constitutes 60% of white matter and 40% of grey matter.",
              "The human brain is very soft like butter.",
              "The Human brain stops growing at the age of 18.",
              "The weight of human cerebellum is 150g.",
              "Your bones are composed of 31% water.",
              "There are 22 bones in the human skull."
       ]
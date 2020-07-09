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
              "Diwali is celebrated on the fifteenth day of the Hindu month of Kartika. Hinduism is a major religion of India, and is considered to be the oldest religion in the world.",
              "More than 800 million people celebrate this festival in various ways.",
              "It is celebrated in honor of Lakshmi – the Hindu goddess of wealth and prosperity.",
              "The festival also marks the return of the Lord Rama and Sita after completing fourteen years in exile.",
              "The word Diwali means “the row of lighted lamps (diyas)” in Hindi.",
              "The festival signifies the victory of light over darkness.",
              "Diwali also marks a major shopping festival in the places where it is celebrated. There are special discounts and offers that businesses provide to their customers. Buying new things during this festival is considered to be good.",
              "It is the most famous, biggest and brightest festival of India, and is celebrated for five days.",
              "It is a national holiday in India, Trinidad & Tobago, Myanmar, Nepal, Mauritius, Guyana, Singapore, Suriname, Malaysia, Sri Lanka and Fiji. And is an optional holiday in Pakistan.",
              "On the same night that Diwali is celebrated, Jains celebrate a festival of lights to mark the attainment of moksha by Mahavira.",
              "Oil and light lamps are used in high numbers in and around peoples’ houses and properties to celebrate the festival. The festival commemorates the lighting that was done to bring Lord Rama and his wife Sita from the forest of Ayodhya.",
              "Diyas light the houses; fireworks illuminate the skies and rangoli decorates the outside Hindu homes. They do this to attract Lakshmi, the goddess of good fortune.",
              "Your eyes are always the same size from birth but your nose and ears never stop growing.",
              "Traditional diyas (light lamps) used during Diwali are earthen lamps, although plastic and metallic diyas have also become available recently. These diyas are filled with ghee or oil, and a cotton wick is used to bear the flame.",
              "The diyas are left burning all night.",
              "Sikhs also celebrate Diwali, as it marks the release of their gurji – Guru Hargobind Sahibji – and 52 other kings and princess of India that were made captives by the mogul emperor Shah Jahan.",
              "It is a tradition to clean the house, making it spotless before entering the New Year.",
              "Businesses also start new accounting books, and farmers end the harvest season. The festival also signals the onset of winter.",
              "Hindus all over the world, and especially in India celebrate the festival by exchanging gifts, wearing new clothes and preparing festive meals.",
              "Idols of Lord Ganesh and Goddess Lakshmi are placed side by side for the prayers and rituals. Lord Ganesh is worshipped first followed by Lord Lakshmi.",
              "Diwali is also celebrated in honor of the marriage of the Lord Vishnu and Goddess Lakshmi. And it also marks the triumph of the Lord Krishna over the demon Naraka. Hindus in Bengal honor the fearsome Goddess Kali on the occasion of Diwali.",
              "The English city of Leicester hosts the biggest Diwali celebrations outside of India."
       ]
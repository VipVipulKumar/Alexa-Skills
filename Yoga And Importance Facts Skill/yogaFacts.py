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
    if intentName == "yogaIntent":
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
    speechOutput =  "Hello , Welcome to YOGA FACTS! " \
                    "You can know interesting facts about YOGA by saying 'tell me facts about yoga'"
    repromptText =  "You can know interesting facts about YOGA by saying 'tell me facts about yoga'"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def factsFunction(intent, session):
    import random
    index = random.randint(0,len(Facts)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "Learn about YOGA. An interesting YOGA FACT :: " + Facts[index] 
    repromptText = "You can know interesting facts about YOGA by saying 'tell me facts about yoga'"
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended!!!"
    speechOutput = "Thank you for using YOGA FACTS Alexa Skills Kit. " \
                    "\nHave a great time!!!"
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
              "Yoga originated in India.",
              "Yoga is one of the oldest physical disciplines in existence.",
              "Yoga is over 5,000 years old.",
              "Yoga was originally practised as a form of healing.",
              "Yoga is inspired by practices in Hinduism, Buddhism and Jainism.",
              "The word yoga means yoke or union.",
              "The earliest Yogis are said to have been intoxicated on the sacred drink soma.",
              "The maximum amount of skin should be exposed to the air while practising yoga.",
              "The best-selling yoga book in English is Light on Yoga: Yoga Dipika by B. K. S Iyengar.",
              "Yoga connects the mind, body and soul.",
              "Yoga combines body postures, breathing and meditation.",
              "The official language of Yoga is Sanskrit.",
              "There are 19 different types of Yoga.",
              "There are 66 official yoga postures.",
              "Yoga breathing is called pranayama.",
              "Yoga hand positions are called mudras.",
              "Yoga improves your immune system.",
              "Mudras affects the flow of prana – life energy within the body.",
              "Chair Yoga is practised by seniors / people with disabilities.",
              "Bikram or hot yoga is practiced in rooms heated to 40°C and 50% humidity.",
              "Jivamukti yoga is performed to music.",
              "A glass of lukewarm water should be drunk before commencing yoga.",
              "In Mysore yoga students are invited to practice whatever postures they please.",
              "Yoga increases self-confidence.",
              "The largest yoga center in Asia is the Markandeya Yoga City in Bali.",
              "Yoga improves concentration and motivation.",
              "Dawn is the best time to practice yoga, because the air contains the most prana – life energy.",
              "Yoga was first introduced in the US in the late 19th century.",
              "The most popular type of Yoga in the US is Hatha Yoga.",
              "Americans spend $5.7 billion a year on yoga classes and Yoga Products.",
              "15.8 Million, or 6.9% of adults in the US practice yoga.",
              "72.2% of US yoga practitioners are women, 27.8% are men.",
              "71.4% of US yoga practitioners are college educated, 27% have postgraduate degrees.",
              "A session should begin with gentler postures, advancing into more difficult ones.",
              "Yoga eases digestion.",
              "Yoga relieves anxiety, depression and stress.",
              "Yoga improves your mood.",
              "Yoga leads to a more positive outlook on life.",
              "Yoga reduces anger and hostility.",
              "Naked yoga is gaining in popularity across Europe and the US.",
              "There should be plenty of ventilation in the room where one practises yoga.",
              "Yoga improves memory.",
              "Yoga helps to make you live longer.",
              "Yoga helps to quit addictions.",
              "Elizabeth Gilbert’s experience with Yoga led to 'Eat Pray Love' which has sold over millions of copies worldwide.",
              "Yoga aids weight loss by improving metabolism.",
              "Yoga reduces cellulite through muscle stretching.",
              "Guarasana or Eagle pose has been said to improve male sexual performance.",
              "Yoga helps you sleep better.",
              "Yoga improves posture.",
              "Yoga can reduces menopausal symptoms such as hot flashes.",
              "Yoga improves balance.",
              "Hasyayoga or Laughter Yoga is practiced in more than 60 countries.",
              "Yoga makes you more graceful.",
              "Yoga improves reactions times.",
              "Yoga prevents migraines.",
              "Yoga delays ageing by stimulating detoxification in the body.",
              "Yoga can alleviate allergy symptoms.",
              "Yoga increases pain tolerance.",
              "Yoga reduces blood pressure and pulse rate.",
              "Yoga helps prevent disease by massaging internal organs.",
              "Yoga heals the body and prevents injuries.",
              "Yoga can prevent Alzheimer’s disease.",
              "Yoga alleviates Asthma symptoms.",
              "Yoga helps people with OCD (Obsessive Compulsive Disorder).",
              "Yoga is best practised on an empty stomach.",
              "Yoga should not be practised in front of a mirror.",
              "Loose clothing should be worn when practising yoga.",
              "The mouth should be closed – breathing though the nose only.",
              "Yoga should be practised in a quiet, dust-free room."
       ]

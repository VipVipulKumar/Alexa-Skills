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
    if intentName == "earthIntent":
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
    speechOutput =  "Hello , Welcome to EARTH FACTS! " \
                    "You can know interesting facts about EARTH by saying 'tell me facts about earth'."
    repromptText =  "You can know interesting facts about EARTH by saying 'tell me facts about earth'."
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def factsFunction(intent, session):
    import random
    index = random.randint(0,len(Facts)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "Learn about EARTH. An interesting EARTH FACT :: " + Facts[index] 
    repromptText = "You can know interesting facts about EARTH by saying 'tell me facts about EARTH'."
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using EARTH FACTS Alexa Skills Kit. " \
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
        "The Earth’s rotation is gradually slowing.",
        "The Earth was once believed to be the centre of the universe.",
        "Earth has a powerful magnetic field.",
        "There is only one natural satellite of the planet Earth.",
        "Earth is the only planet not named after a god.",
        "The Earth is the densest planet in the Solar System.",
        "70% of the Earth’s surface is covered in water.",
        "Earth is mostly iron, oxygen and silicon.",
        "Earth doesn’t take 24 hours to rotate on its axis. It’s actually 23 hours, 56 minutes and 4 seconds.",
        "A year on Earth isn’t 365 days. It’s actually 365.2564 days.",
        "Earth has 1 moon and 2 co-orbital satellite.",
        "The Earth tilts at roughly 66 degrees.",
        "Only 3% water of the earth is fresh, rest 97% salted. Of that 3%, over 2% is frozen in ice sheets and glaciers. Means less than 1% fresh water is found in lakes, rivers and underground.",
        "Asia Continent is covered 30% of the total earth land area, but represent 60% of the world’s population.",
        "Each winter there are about 1 septillion (1, 000, 000, 000, 000, 000, 000, 000, 000 or a trillion trillion) snow crystals that drop from the sky.",
        "The Earth was formed approximately 4.54 billion years ago and is the only known planet to support life.",
        "The third planet from the sun, Earth is the only place in the known universe confirmed to host life.",
        "With a radius of 3,959 miles, Earth is the fifth largest planet in our solar system.",
        "Earth zooms through its orbit at an average velocity of 18.5 miles a second.",
        "Earth's orbit around the sun, giving us seasons.",
        "Whichever hemisphere is tilted closer to the sun experiences summer, while the hemisphere tilted away gets winter.",
        "Earth's crust and upper mantle are divided into massive plates that grind against each other in slow motion.",
        "As these plates collide, tear apart, or slide past each other, they give rise to our very active geology.",
        "Many volcanoes form as seafloor crust smashes into and slides beneath continental crust.",
        "When plates of continental crust collide, mountain ranges such as the Himalaya are pushed toward the skies.",
        "Earth's atmosphere is 78 percent nitrogen, 21 percent oxygen, and one percent other gases such as carbon dioxide, water vapor, and argon.",
        "Earth's surface temperature is about 57 degrees Fahrenheit; without our atmosphere, it'd be zero degrees.",
        "In the last two centuries, humans have added enough greenhouse gases to the atmosphere to raise Earth's average temperature by 1.8 degrees Fahrenheit. This extra heat has altered Earth's weather patterns in many ways.",
        "The atmosphere not only nourishes life on Earth, but it also protects it: It's thick enough that many meteorites burn up before impact from friction, and its gases—such as ozone—block DNA-damaging ultraviolet light from reaching the surface.",
        "We enjoy protection from Earth's magnetic field, generated by our planet's rotation and its iron-nickel core. This teardrop-shaped field shields Earth from high-energy particles launched at us from the sun and elsewhere in the cosmos.",
        "Thanks to instruments such as NASA's Kepler Space Telescope, astronomers have found more than 3,800 planets orbiting other stars, some of which are about the size of Earth, and a handful of which orbit in the zones around their stars that are just the right temperature to be potentially habitable.",
        "The first photo of Earth from space has been taken on 1946."
    ]

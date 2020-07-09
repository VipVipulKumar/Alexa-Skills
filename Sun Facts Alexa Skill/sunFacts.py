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
    if intentName == "sunIntent":
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
    speechOutput =  "Hello , Welcome to SUN FACTS! " \
                    "You can know interesting facts about SUN by saying 'tell me facts about sun'."
    repromptText =  "You can know interesting facts about SUN by saying 'tell me facts about sun'."
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def factsFunction(intent, session):
    import random
    index = random.randint(0,len(Facts)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "Learn about SUN. An interesting SUN FACT :: " + Facts[index] 
    repromptText = "You can know interesting facts about SUN by saying 'tell me facts about SUN'."
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using SUN FACTS Alexa Skills Kit. " \
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
        "The Sun accounts for 99.86% of the mass in the solar system. It has a mass of around 330,000 times that of Earth. It is three quarters hydrogen and most of its remaining mass is helium.",
        "Over one million Earth’s could fit inside the Sun. If you were to fill a hollow Sun with spherical Earths, somewhere around 960,000 would fit inside. However, if you squashed those Earths to ensure there was no wasted space then you could fit 1,300,000 Earths inside the Sun. The surface area of the Sun is 11,990 times that of Earth.",
        "One day the Sun will consume the Earth. The Sun will continue to burn for about 130 million years after it burns through all of its hydrogen, instead burning helium. During this time it will expand to such a size that it will engulf Mercury, Venus, and Earth. When it reaches this point, it will have become a red giant star.",
        "The energy created by the Sun’s core is nuclear fusion. This huge amount of energy is produced when four hydrogen nuclei are combined into one helium nucleus.",
        "The Sun is almost a perfect sphere. Considering the sheer size of the Sun, there is only a 10 km difference in its polar and equatorial diameters – this makes it the closest thing to a perfect sphere observed in nature.",
        "The Sun is travelling at 220 km per second. It is around 24,000-26,000 light-years from the galactic centre and it takes the Sun approximately 225-250 million years to complete one orbit of the centre of the Milky Way.",
        "The Sun will eventually be about the size of Earth. Once the Sun has completed its red giant phase, it will collapse. It’s huge mass will be retained, but it will have a volume similar to that of Earth. When that happens, it will be known as a white dwarf.",
        "It takes eight minutes for light reach Earth from the Sun. The average distance from the Sun to the Earth is about 150 million km. Light travels at 300,000 km per second so dividing one by the other gives you 500 seconds – eight minutes and twenty seconds. This energy can reach Earth in mere minutes, but it takes millions of years to travel from the Sun’s core to its surface.",
        "The Sun is halfway through its life. At 4.5 billion years old, the Sun has burned off around half of its hydrogen stores and has enough left to continue burning hydrogen for another 5 billion years. Currently the Sun is a yellow dwarf star.",
        "The distance between Earth and Sun changes. This is because the Earth travels on a elliptical orbit path around the Sun. The distance between the two ranges from 147 to 152 million km. This distance between them is one Astronomical Unit (AU).",
        "The Sun rotates in the opposite direction to Earth with the Sun rotating from west to east instead of east to west like Earth.",
        "The Sun rotates more quickly at its equator than it does close to its poles. This is known as differential rotation.",
        "The Sun has a powerful magnetic field. When magnetic energy is released by the Sun during magnetic storms, solar flares occur which we see on Earth as sunspots. Sunspots are dark areas on the Sun’s surface caused by magnetic variations. The reason they appear dark is due to their temperature being much lower than surrounding areas.",
        "Temperatures inside the Sun can reach 15 million degrees Celsius. Energy is generated through nuclear fusion in the Sun’s core – this is when hydrogen converts to helium – and because objects generally expand, the Sun would explode like an enormous bomb if it wasn’t for it’s tremendous gravitational pull.",
        "The Sun generates solar winds. These are ejections of plasma (extremely hot charged particles) that originate in the layer of the Sun know as the corona and they can travel through the solar system at up to 450 km per second.",
        "The atmosphere of the Sun is composed of three layers: the photosphere, the chromosphere, and the corona.The Sun is classified as a yellow dwarf star. It is a main sequence star with surface temperatures between 5,000 and 5,700 degrees celsius (9,000 and 10,300 degrees fahrenheit).",
        "The Aurora Borealis and Aurora Australis are caused by the interaction of solar winds with Earth’s atmosphere.",
        "While our Sun does not have an official scientific name, it does have another common name: Sol. This name originates from the ancient Roman’s god of the Sun, Sol. This alternate name is where we get the term 'solar system,' which literally means system of the Sun.",
        "Sun is about 4.5 billion years old.",
        "Sun is the largest object in the solar system.",
        "Helioseismology is the study of the interior of the sun.",
        "There are electric currents inside of it that generate a magnetic field which spreads throughout the solar system.",
        "The suns UV rays also have antiseptic properties.",
        "The amount of energy released during a flare is equivalent to a simultaneous explosion of millions of 100-megaton hydrogen bombs.",
        "This explosion is ten million times greater than a volcanic eruption but less than 1/10th of the total energy emitted by the sun per second.",
        "The sun is actually a mixture of ALL colors, which appears to the eye as white.",
        "It seems to be several different colors during the day due to a phenomenon known as atmospheric scattering.",
        "A green flash is a short lived optical illusion that sometimes occurs at sunrise or sunset when the light from the sun is bent towards the viewer.",
        "It is as bright as 4 trillion trillion 100-watt light bulbs.",
        "The Sun does not have any rings.",
        "Partial solar eclipses are dangerous to the naked eye because our pupils are not accustomed to that level of contrast in light.",
        "Some parts of the sun are cooler than others and thus appear to be darker. They are called sunspots.",
        "Sun spots have a very strong magnet field, which prevents the convection of energy, and thus accounts for their lower temperatures.",
        "In fact, the sun is about 400 times larger than the moon.",
        "A typical sunspot consists of a dark spot in the middle called the umbra, and a lighter region known as the penumbra.",
        "The solar maximum is a period of time during the solar cycle when the number of sunspots is at its highest."
    ]



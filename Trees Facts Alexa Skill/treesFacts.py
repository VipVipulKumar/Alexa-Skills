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
    if intentName == "treesIntent":
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
    speechOutput =  "Hello , Welcome to TREES FACTS! " \
                    "You can know interesting facts about TREES by saying 'tell me facts about trees'."
    repromptText =  "You can know interesting facts about TREES by saying 'tell me facts about trees'."
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def factsFunction(intent, session):
    import random
    index = random.randint(0,len(Facts)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "Learn about TREES. An interesting TREES FACT :: " + Facts[index] 
    repromptText = "You can know interesting facts about TREES by saying 'tell me facts about TREES'."
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using TREES FACTS Alexa Skills Kit. " \
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
            "Trees are the longest living organisms on Earth, and never die of old age. The Old List is a database of ancient trees that officially tracks old trees, their species, and location. Methuselah, from California’s White Mountains, comes in at over 4,800 years old.",
            "Just like humans, trees need water to survive--and they drink a lot of it. In a single day, a large tree can consume 100 gallons of water out of the ground and discharge it into the air as oxygen and water vapor. Keep in mind that many conditions play a role such as the size of the tree, species of the tree, humidity, temperatures, sun exposure, etc.",
            "Strategically planting trees and shrubs can save you up to 25 percent on your energy bills. Not only do they provide shade in the summer, but serve as a windbreak in the winter, too.",
            "'Moon trees' were grown from seeds taken to the moon in early 1971. After orbiting the earth with the Apollo 14 mission, these tree seeds returned to earth and were germinated by the Forest Service. After being planted with their earth-bound counterparts, these seedlings showed no discernible difference after twenty years of growth.",
            "Trees are able to communicate and defend themselves against attacking insects. Scientists have found that trees can flood their leaves with chemicals called phenolics when the insects begin their raid. They can also signal danger to other trees so they can start their own defense.",
            "Pine cones have genders. Male pine cones shed pollen and female pine cones make seeds. When the wind blows pollen into the female cones, you guessed it, the seeds become pollinated.",
            "The 'knock on wood' tradition comes from a time when primitive pagans used to tap or knock on trees to summon the protective spirits that resided in them.",
            "A tree can absorb as much as 48 pounds of carbon dioxide each year and can sequester 1 ton of carbon dioxide by the time it reaches 40 years old. It is estimated that United States forests absorb about 10% of the country’s CO2 emissions each year.",
            " Trees can help you find your way if you get lost in the woods. In northern temperate climates, moss will grow on the northern side of the tree trunk, where there is more shade. Also, a tree’s rings can help point you in the right direction too. If you’re in the northern hemisphere, you can see the rings of the tree grow slightly thicker on the southern side since it receives more sunlight. In the southern hemisphere, the opposite is true, with rings being thicker on the northern side.",
            "Pine trees grow on six of seven continents, with Antarctica being the only one left out.",
            "Trees lower air temperature by evaporating water in their leaves.",
            "If a birdhouse is hung on a tree branch, it does not move up the tree as the tree grows.",
            "Trees improve water quality by slowing and filtering rainwater and protecting aquifers and watersheds.",
            "The different parts of a tree grow at different times throughout the year. Typically, most of the foliage growth happens in the spring, followed by trunk growth in the summer and root growth in the fall and winter.",
            "Earth has more than 60,000 known tree species.",
            "More than half of all tree species exist only in a single country. Brazil, Colombia and Indonesia have the highest totals for endemic tree species, which makes sense given the overall biodiversity found in their native forests.",
            "Trees didn't exist for the first 90 percent of Earth's history.",
            "Before trees, Earth was home to fungi that grew 26 feet tall.",
            "The first known tree was a leafless, fern-like plant from New York.",
            "Scientists thought this dinosaur-era tree went extinct 150 million years age, but then it was found growing wild in Australia. Species, Wollemia nobilis, is often described as a living fossil. Only about 80 mature trees are left, plus some 300 seedlings and juveniles, and the species is listed as critically endangered by the International Union for Conservation of Nature.",
            "Some trees emit chemicals that attract enemies of their enemies.",
            "Trees in a forest can 'talk' and share nutrients through an underground internet built by soil fungi.",
            "Most tree roots stay in the top 18 inches of soil, but they can also grow above ground or dive a few hundred feet deep.",
            "A large oak tree can consume about 100 gallons of water per day, and a giant sequoia can drink up to 500 gallons daily.",
            "Trees help us breathe — and not just by producing oxygen.",
            "Adding one tree to an open pasture can increase its bird biodiversity from almost zero species to as high as 80.",
            "Trees can lower stress, raise property values and fight crime.",
            "North America's bristlecone pines are especially long-lived, and one in California that's 4,848 years old was considered the planet's oldest individual tree until 2013, when researchers announced they'd found a another bristlecone that sprouted 5,062 years ago.",
            "A large oak tree can drop 10,000 acorns in one year."
    ]

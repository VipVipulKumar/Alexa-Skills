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
    if intentName == "whatispetfun":
        return fun_pet(intent, session)
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
    cardTitle = " Hello"
    speechOutput =  "Hello , Welcome to PET MONSTER FACTS! " \
                    "You can know interesting facts about PET MONSTER by saying 'tell me about pet monster facts'"
    repromptText =  "You can know interesting facts about PET MONSTER by saying 'tell me about pet monster facts'"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def fun_pet(intent, session):
    import random
    index = random.randint(0,len(monster_pet)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "Learn about PET MONSTER. An interesting PET MONSTER FACT :: " + monster_pet[index] 
    repromptText = "You can know interesting facts about PET MONSTER by saying 'tell me about pet monster facts'"
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using pet monster facts Alexa Skills Kit. " \
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



monster_pet = [ "Rhydon was the first Pokemon ever created.",
            "Pikachu's name is Japanese onomatopoeia for sparkle and squeaking.",
            "Drowzee is based off of a tapir.",
            "Azurill is the only Pokemon that can change gender.",
            "Psychic type Pokemon are weak to bug, ghost, and dark type because they're common fears.",
            "Rock types could still beat a Pokemon with all 18 types.",
            "Xatu sees both past and future at the same time.",
            "Slowbro is the only Pokemon that can devolve.",
            "Slowpoke is considered a delicacy.",
            "Many Pokemon names include numbers.",
            "Cubone wears the skull of his dead mother.",
            "Poliwag's swirl is based on tadpoles intestines.",
            "Pokemon is short for Pocket Monster.",
            "Yamask is a dead human.",
            "Munna was mentioned in the first game.",
            "Hitmonchan and Hitmonlee got their names from famous fighters.",
            "Arcanine was intended to be a legendary Pokemon.",
            "The move Splash is a mistranslation for Hop.",
            "Pikachu and Meowth are exact opposites.",
            "Clefairy was almost the face of Pokemon.",
            "Ditto was a failed attempt to copy Mew.",
            "Each Spinda has a unique pattern of spots.",
            "Fishing is possible in Pokemon red and blue gyms.",
            "Smeargle can use almost every move in the game.",
            "Wobuffet's main body is a decoy.",
            "The Pokémon Drowzee is based on the tapir. According to Japanese folklore, tapirs eat dreams and nightmares.",
            "When Paras evolves into Parasect, the parasitic mushroom on its back actually takes over the host, which explains the Pokémon's blank, white eyes.",
            "The electric-type sheep Pokémon Mareep is thought to be a reference to Do Androids Dream of Electric Sheep? by Phillip K. Dick.",
            "The Pokémon Koffing and Weezing were originally going to be named 'Ny' and 'La' because of the smog that New York and Los Angeles are known for.",
            "One of Farfetch'd's Pokédex entries implies that humans nearly hunted the Pokémon into extinction, which confirms that people in the Pokémon universe eat Pokémon.",
            "Pikachu's name is a combination of the Japanese onomatopoeia for sparkle, pikapika, and the sound of squeaking, which is expressed as chuchu.",
            "Magneton is made up of three Magnemites and should logically weigh three times as much, but Magnemite weighs in at 13.2 pounds and Magneton weighs 132 pounds.",
            "The various settings in the Pokémon games before Generation IV all seem to resemble real-world locations in Japan.",
            "There's a theory that right before the games, the world of Pokémon was embroiled in a massive war.",
            "There's a theory that the faces on Vanillite, Vanillish, and Vanilluxe are decoys, and the ice crystals seen near their false faces are their actual facial features.",
            "Some Pokémon go through major evolutions after being traded.",
            "The location Lavender Town is known to cause a sense of uneasiness in some players.",
            "Vullaby is labeled as a dark-type Pokémon in the Pokédex, due to that fact that it appears to be wearing a human skull."
        ]

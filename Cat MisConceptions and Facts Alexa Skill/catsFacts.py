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
    if intentName == "catIntent":
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
    speechOutput =  "Hello , Welcome to CATS FACTS! " \
                    "You can know interesting facts about CATS by saying 'tell me facts about cats'."
    repromptText =  "You can know interesting facts about CATS by saying 'tell me facts about cats'."
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def factsFunction(intent, session):
    import random
    index = random.randint(0,len(Facts)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "Learn about CATS. An interesting CAT FACT :: " + Facts[index] 
    repromptText = "You can know interesting facts about CATS by saying 'tell me facts about cats'."
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using CATS FACTS Alexa Skills Kit. " \
                    "Have a great time! MEOW!!!"
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
		"Cats are the most popular pet in the United States: There are 88 million pet cats and 74 million dogs.",
		"There are cats who have survived falls from over 32 stories (320 meters) onto concrete.",
		"A group of cats is called a clowder.",
		"Cats have over 20 muscles that control their ears.",
		"Cats sleep 70% of their lives.",
		"A cat has been mayor of Talkeetna, Alaska, for 15 years. His name is Stubbs.",
		"In tigers and tabbies, the middle of the tongue is covered in backward-pointing spines, used for breaking off and gripping meat.",
		"When cats grimace, they are usually 'taste-scenting.' They have an extra organ that, with some breathing control, allows the cats to taste-sense the air.",
		"Cats can't taste sweetness.",
		"Owning a cat can reduce the risk of stroke and heart attack by a third.",
		"The world's largest cat measured 48.5 inches long.",
		"Evidence suggests domesticated cats have been around since 3600 B.C., 2,000 years before Egypt's pharaohs.",
		"A cat's purr may be a form of self-healing, as it can be a sign of nervousness as well as contentment.",
		"Similarly, the frequency of a domestic cat's purr is the same at which muscles and bones repair themselves.",
		"Adult cats only meow to communicate with humans.",
		"The world's richest cat is worth $13 million after his human passed away and left her fortune to him.",
		"Your cat recognizes your voice but just acts too cool to care (probably because they are).",
		"Cats are often lactose intolerant, so stop givin' them milk!",
		"Basically all cartoon cats lied to us: Raw fish is off the table for cats as well.",
		"The oldest cat video on YouTube dates back to 1894 (when it was made, not when it was uploaded, duh).",
		"In the 1960s, the CIA tried to turn a cat into a bonafide spy by implanting a microphone into her ear and a radio transmitter at the base of her skull. She somehow survived the surgery but got hit by a taxi on her first mission.",
		"The technical term for 'hairball' is 'bezoar.'",
		"Female cats are typically right-pawed while male cats are typically left-pawed.",
		"Cats make more than 100 different sounds whereas dogs make around 10.",
		"A cat's brain is 90% similar to a human's — more similar than to a dog's.",
		"Cats and humans have nearly identical sections of the brain that control emotion.",
		"A cat's cerebral cortex (the part of the brain in charge of cognitive information processing) has 300 million neurons, compared with a dog's 160 million.",
		"Cats have a longer-term memory than dogs, especially when they learn by actually doing rather than simply seeing.",
		"Basically, cats have a lower social IQ than dogs but can solve more difficult cognitive problems when they feel like it.",
		"Cats have 1,000 times more data storage than an iPad.",
		"It was illegal to slay cats in ancient Egypt, in large part because they provided the great service of controlling the rat population.",
		"In the 15th century, Pope Innocent VIII began ordering the killing of cats, pronouncing them demonic.",
		"A cat has five toes on his front paws, and four on the back, unless he's a polydactyl.",
		"Polydactyl cats are also referred to as 'Hemingway cats' because the author was so fond of them.",
		"There are 45 Hemingway cats living at the author's former home in Key West, Fla.",
		"Original kitty litter was made out of sand but it was replaced by more absorbent clay in 1948.",
		"Abraham Lincoln kept four cats in the White House.",
		"Isaac Newton is credited with inventing the cat door.",
		"One legend claims that cats were created when a lion on Noah's Ark sneezed and two kittens came out.",
		"A cat can jump up to six times its length.",
		"A house cat is faster than Usain Bolt.",
		"When cats leave their poop uncovered, it is a sign of aggression to let you know they don't fear you.",
		"Cats can change their meow to manipulate a human. They often imitate a human baby when they need food, for example.",
		"Cats use their whiskers to detect if they can fit through a space.",
		"Cats only sweat through their foot pads.",
		"The first cat in space was French. She was named Felicette, or 'Astrocat'. She survived the trip.",
		"Cats have free-floating clavicle bones that attach their shoulders to their forelimbs, which allows them to squeeze through very small spaces.",
		"Hearing is the strongest of cat's senses: They can hear sounds as high as 64 kHz — compared with humans, who can hear only as high as 20 kHz.",
		"Cats can move their ears 180 degrees.",
		"Cats can also move their ears separately.",
		"A cat has detected his human's breast cancer.",
		"A cat's nose is ridged with a unique pattern, just like a human fingerprint.",
		"Cats have scent glands along their tail, their forehead, lips, chin, and the underside of their front paws.",
		"A cat rubs against people to mark its territory.",
		"Cats lick themselves to get your scent off.",
		"When a family cat died in ancient Egypt, family members would shave off their eyebrows as they mourned.",
		"They also had elaborate memorials that included mummifying the cat and either burying it in a family tomb or pet cemetery.",
		"Cats were mythic symbols of divinity in ancient Egypt.",
		"Black cats are bad luck in the United States, but they are good luck in the United Kingdom and Australia.",
		"Most cats don't like water because their coats do not insulate them well enough.",
		"The Egyptian Mau is the oldest breed of cat.",
		"The Egyptian Mau is also the fastest pedigreed cat.",
		"The Egyptian word for cat is, in fact, 'mau'.",
		"Only 11.5% of people consider themselves 'cat people'.",
		"Cat people are also 11% more likely to be introverted.",
		"Cat owners who are male tend to be luckier in love, as they are perceived as more sensitive.",
		"A cat's carbon footprint is similar to that of a VW Bug, whereas a dog's is more like a Hummer.",
		"Cats have inferior daytime sight, but during the night they need seven times less light than humans to see.",
		"The largest litter of kittens produced 19 kittens.",
		"Eighty-eight percent of cats in the U.S. are spayed or neutered.",
		"Only 24% of cats who enter animal shelters are adopted.",
		"Cats are really cool.",
		"Cats are very soft.",
		"Unlike dogs, cats do not have a sweet tooth. Scientists believe this is due to a mutation in a key taste receptor.",
		"When a cat chases its prey, it keeps its head level. Dogs and humans bob their heads up and down.",
		"A cat can’t climb head first down a tree because every claw on a cat’s paw points the same way. To get down from a tree, a cat must back down.",
		"Cats make about 100 different sounds. Dogs make only about 10.",
		"Every year, nearly four million cats are eaten in Asia.",
		"There are more than 500 million domestic cats in the world, with approximately 40 recognized breeds.",
		"Approximately 24 cat skins can make a coat.",
		"The group of words associated with cat (catt, cath, chat, katze) stem from the Latin catus, meaning domestic cat, as opposed to feles, or wild cat.",
		"Approximately 40,000 people are bitten by cats in the U.S. annually.",
		"Researchers are unsure exactly how a cat purrs. Most veterinarians believe that a cat purrs by vibrating vocal folds deep in the throat. To do this, a muscle in the larynx opens and closes the air passage about 25 times per second.",
		"Most cats give birth to a litter of between one and nine kittens. The largest known litter ever produced was 19 kittens, of which 15 survived."
		]
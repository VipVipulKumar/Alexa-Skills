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
    if intentName == "shivIntent":
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
    speechOutput =  "Hello, Welcome to SHIV KOSH! " \
                    "You can know interesting facts about Lord Shiva by saying 'tell me facts about lord Shiva'"
    repromptText =  "You can know interesting facts about Lord Shiva by saying 'tell me facts about lord Shiva'"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def factsFunction(intent, session):
    import random
    index = random.randint(0,len(Facts)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "SHIV KOSH GYAAN. An interesting LORD SHIVA FACT :: " + Facts[index] 
    repromptText = "You can know interesting facts about Lord Shiva by saying 'tell me facts about lord Shiva'"
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using Shiv Kosh Alexa Skills Kit. " \
                   "Have a great time!"
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
			"Hanuman, son of Anjana and Kesari, is actually an avatar of Lord Shiva. It is believed that Hanuman is the eleventh avatar of Lord Shiva. Several texts present him as an incarnation of the god Shiva. Known for his devotion to Lord Rama, the son of Anjana and Kesari, blessed by the Hindu God of wind, Vayu, Hanuman is celebrated for his devotion to Lord Rama.",
			"Ravana, the primary antagonist in the Hindu epic Ramayana, was one of the greatest devotees of Lord Shiva. It is said, when Ravana tried to uproot Mount Kailash, Shiva trapped him beneath Kailash. To redeem himself, Ravana started pleasing Shiva by singing hymns and playing instruments. Eventually, over many years, Shiva freed him from under the mountain and blessed him.",
			"Even Kamadeva, the Hindu God of love and Cupid's equivalent, could not distract Shiva successfully with his tricks. He had to face the consequence when he tried to. When Devas were waging a war against Tarakasur, they needed Shiva's help but Shiva was busy meditating. So the Devas asked Kamadeva to pierce Shiva with his love arrows. But Shiva, who was in deep meditation, woke up in rage and burned Kamadeva down to ashes with his third eye.",
			"Lord Shiva's first wife Sati killed herself because she was frustrated with her father who insulted Shiva. Shiva took his revenge and how. As per mythology, Sati, and not Parvati, (as most of us may not know), was the first wife of Shiva and was very fond of him. The daughter of a priest, her father did not approve of the ways of Shiva. When Sati's father decided to perform a sacrifice, he invited everyone except for Shiva. This move to insult Shiva really bothered her and she killed herself in the sacrifice. A furious Shiva killed her father in a rage.",
			"The snake around Shiva's neck reinforces a sense of stillness. The mountains, snow and the snake around Lord Shiva's neck is a symbol representing his sense of calmness. Self-contained and content, Shiva is a symbol of calm and peace.",
			"Shiva's Trishul or Trident symbolizes the unity of three worlds. The Trident or Trishul of Lord Shiva unites the three worlds a human being is associated with - his inside world, the immediate world around him and the broader world. The trident shows a harmony between the three.",
			"Ganja/Cannabis is one of the primary offerings in Shiva's worship. On the auspicious day of Shivaratri, the Shaivites, a sect of followers, consume Bhang (a beverage prepared from cannabis) and smoke weed. Popular among the followers, this is one hell of an offering for a God!",
			"Shiva takes the form of Nataraja to suppress Apasmara - the symbol of ignorance.It is believed, the dwarf demon 'Apasmara', who represented ignorance challenged Lord Shiva. It was then that Lord Shiva took the form of Nataraja and performed the famous Tandava or the dance of destruction, eventually crushing the arrogant Apasmara under his right foot. Since Apasmara (ignorance) should not die to preserve the balance between knowledge and ignorance, it is believed that Lord Shiva forever remains in his Nataraja form suppressing Apasmara for eternity. His Nataraja avatar is a message that ignorance can only be overcome by knowledge, music, and dance.",
			"Ardhanarishwar is Shiva's androgynous form. Often cited as an example of perfect marriage, Shiva along with his consort Parvati is represented in the Ardhanarishwar form - which is a half male and half female icon. It is believed that this androgynous form shows that the masculine energy (Purusha) and feminine energy (Prakrithi) of the universe in a synthesis.",
			"Shiva accepted Nandi, who was offered to Him by other Gods, as his doorkeeper and his vehicle. As the story goes, Surabhi, the mother of all cows started giving birth to a lot of cows, and the cows started flooding Kailash with their milk. Furious at this, Shiva used his third eye and destroyed many of them. To calm him down, the Gods sought to offer Nandi the magnificent bull to Lord Shiva.",
			"In stories, Lord Shiva is naked and sports an erect phallus. According to Devdutt Pattanaik, in Epified, Shiva is naked and sports an erect phallus in almost all the stories. It is to save the public from discomfort that he clothes himself in an animal hide. According to Pattanaik, Shiva being content and disconnected from the outside world is aroused not by external stimulation but by perpetual internal bliss.",
			"The ash Shiva is smeared with symbolizes permanence and destruction. Like we all know, Shiva is smeared with ash. It is a symbol of destruction as well as permanence for it is created by burning things but cannot be burnt itself. It is a symbol indicating the permanence of the immortal soul, which is released when the matter is destroyed.",
			"The three lines of ash on his forehead refers to destruction of the three worlds. Shiva has three lines of ash smeared on his forehead in a horizontal orientation. The lines represent the destruction of the three worlds of Hinduism. It suggests inertia and lack of movement and refers to the merging of the three worlds to become one with the self.",
			"Shiva has a blue throat because he drank Halahala poison during the churning of the milky ocean. . The Devas and Asuras started churning the milky ocean in order to obtain Amrit. In the process, they found a fatal poison - the Halahala poison, that had to be sucked out of the ocean. Without thinking of the consequences, Shiva drank all the poison and Parvati pressed his throat in order to stop the poison from spreading to other parts of his body - which is the reason behind his blue throat.",
			"The  story of the infinite pillar of fire - when Brahma and Vishnu fought over who the real God was, Shiva made it clear who it really was.. In a conflict between Brahma and Vishnu regarding who the real God was, Shiva appeared as an infinite Linga fire-pillar. Determined to find the ends of the pillar, Vishnu as Varaha tried to find the bottom of the Linga while Brahma tried to find its top. Vishnu came back and admitted that the pillar was endless. Brahma, however, lied about the pillar's limits and claimed that he was the true God. Just then, the pillar broke open and Shiva appeared. Accusing Brahma of lying and denying he is a God, he appreciated Vishnu for his honesty and suggested that Vishnu was on his way to becoming a God - in the process stating that he was the one true God.",
			"According to a Hindu legend, Shiva explained the secret of life and eternity in the Amarnath Cave to Parvati. It is believed, this is the cave where Shiva explained the secret of life and eternity to his divine consort, Parvati. Every year, followers and devotees of Lord Shiva pay their visit to the famous Amarnath cave. The cave also houses an ice stalagmite Lingam.",
			"Shiva was attracted to Vishnu's female form, Mohini, as a result of which Ayyappa was born. In the Bhagavata Purana, after Vishnu deceived the demons in his female form, Shiva wanted to see the bewildering Mohini again. When Vishnu agreed and revealed his Mohini form, Shiva got lured by Mohini, while the abandoned wife Parvati looked on. Shiva is overcome by Kama (love and desire). His 'unfailing' seed escaped and fell on the ground. From these seeds of Shiva, Ayyappa was born.",
			"Shiva calmly trapped Ganga back in his hair because of her arrogance. He let her out but in small streams. As it goes, Bhagiratha asked Brahma to bring the river Ganges down to earth so that he could perform a ceremony for his ancestors. Brahma asked Bhagiratha to propitiate Lord Shiva, for only Shiva could break Ganga's landfall. Ganga arrogantly flew down to earth but Shiva calmly trapped her back in his hair and let her out in small streams. It is said, the touch of Shiva further sanctified Ganga.",
			"Lord Shiva punished one crore Gods and Goddesses for not waking up on time and turned them into stone images. As per Hindu mythology, Lord Shiva was on his way to Kashi along with one crore gods and goddesses. He asked all of them to wake up before sunrise the following day, before taking a night's rest in Unakoti, Tripura. But in the morning, no one except Shiva woke up. This made him furious and he set out for Kashi on his own, cursing the others to become stone images."
		]

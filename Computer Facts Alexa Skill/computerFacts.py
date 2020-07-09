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
    if intentName == "computerIntent":
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
    speechOutput =  "Hello , Welcome to COMPUTER FACTS! " \
                    "You can know interesting facts about COMPUTER by saying 'tell me facts about computer'."
    repromptText =  "You can know interesting facts about COMPUTER by saying 'tell me facts about computer'."
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def factsFunction(intent, session):
    import random
    index = random.randint(0,len(Facts)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "Learn about COMPUTER. An interesting COMPUTER FACT :: " + Facts[index] 
    repromptText = "You can know interesting facts about COMPUTER by saying 'tell me facts about COMPUTER'."
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using COMPUTER FACTS Alexa Skills Kit. " \
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
        "The first electronic computer ENIAC weighed more than 27 tons and took up 1800 square feet.",
        "Only about 10% of the world’s currency is physical money, the rest only exists on computers.",
        "TYPEWRITER is the longest word that you can write using the letters only on one row of the keyboard of your computer.",
        "Doug Engelbart invented the first computer mouse in around 1964 which was made of wood.",
        "There are more than 5000 new computer viruses are released every month.",
        "Around 50% of all Wikipedia vandalism is caught by a single computer program with more than 90% accuracy.",
        "If there was a computer as powerful as the human brain, it would be able to do 38 thousand trillion operations per second and hold more than 3580 terabytes of memory.",
        "The password for the computer controls of nuclear tipped missiles of the U.S was 00000000 for eight years.",
        "Approximately 70% of virus writers are said to work under contract for organized crime syndicates.",
        "HP, Microsoft and Apple have one very interesting thing in common – they were all started in a garage.",
        "An average person normally blinks 20 times a minute, but when using a computer he/she blinks only 7 times a minute.",
        "The house where Bill Gates lives, was designed using a Macintosh computer.",
        "The first ever hard disk drive was made in 1979, and could hold only 5MB of data.",
        "The first 1GB hard disk drive was announced in 1980 which weighed about 550 pounds, and had a price tag of $40,000.",
        "More than 80% of the emails sent daily are spams.",
        "A group of 12 engineers designed IBM PC and they were called as 'The Dirty Dozen'.",
        "The original name of windows was Interface Manager.",
        "The first microprocessor created by Intel was the 4004. It was designed for a calculator, and in that time nobody imagined where it would lead.",
        "IBM 5120 from 1980 was the heaviest desktop computer ever made. It weighed about 105 pounds, not including the 130 pounds external floppy drive.",
        "Genesis Device demonstration video in Star Trek II: The Wrath of Khan was the the first entirely computer generated movie sequence in the history of cinema. That studio later become Pixar.",
        "A computer worm was present before that could access your Windows XP OS, could download a patch from Microsoft to exist the vulnerability as used it to infect the system and after delete itself.",
        "Amazon was a hard cover book seller, but actually now sells more e-books than hard covers.",
        "The fact that keyboard have ‘Q’ ‘W’ ‘E’ ‘R’ ‘T’ ‘Y’ types of button: When keyboard was invented, it had buttons in alphabetical order, as a result, the typing speed was too fast and the computer used to hang. So, to reduce the speed of a person, qwerty keyboard were invented.",
        "In 2005, Sony illegally installed rootkits on 22 million computers to prevent the users from ripping copyrighted music, and could not be uninstalled. It also reported user’s listening habits back to Sony. Ironically, the code itself contained open source software, and so infringed copyright.",
        "2012 was the year a hacker group took down Pope John’s website because a food company spent over two hours to deliver as expected. The hacker group was called UGNazi.",
        "In Windows 98, minimized windows are actually moved far away outside the average monitor’s resolution.",
        "It took Pixar 29 hours to render a single frame from Monster’s University. If done on a single CPU it would have taken 10,000 years to finish.",
        "IBM 5120 from 1980 was the heaviest desktop computer ever made. It weighed about 105 pounds, not including the 130 pounds external floppy drive.",
        "A 15 year old hacked NASA computers and caused a 21-day shutdown of their computers.",
        "The computer in your cell phone today is million times cheaper and a thousands times more powerful and about a hundred thousands times smaller than the one computer at MIT in 1965.",
        "In 1960, the computer at NORAD warned with 99.9% certainty that the Soviets had just launched a full-scale missile attack against North America. NORAD later discovered that the Early Warning System in Greenland had interpreted the moon rising over Norway as a missile attack from Siberia.",
        "In 1833, Charles Babbage invented all the parts a modern computer uses, but it wasn’t until 120 years later that the first modern computers were invented.",
        "There are more than 5000 new computer viruses are released every month.",
        "Web Arx security says more than 20,000 websites are hacked each day and most from the US.",
        "YouTube was founded by 3 former employees of PayPal.",
        "In 2012, the founder of McAfee Antivirus, John McAfee was asked if he personally uses McAfee anti-virus, he replied by saying 'I take it off,' and that 'It’s too annoying.'"
    ]


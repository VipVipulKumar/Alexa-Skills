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
    if intentName == "girlIntent":
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
    speechOutput =  "Hello , Welcome to GIRLS FACTS! " \
                    "You can know interesting facts about GIRLS by saying 'tell me facts about girls'."
    repromptText =  "You can know interesting facts about GIRLS by saying 'tell me facts about girls'."
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def factsFunction(intent, session):
    import random
    index = random.randint(0,len(Facts)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "Girls' Diaries. An interesting FACT about Girls :: " + Facts[index] 
    repromptText = "You can know interesting facts about GIRLS by saying 'tell me facts about girls'."
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended!!!"
    speechOutput = "Don't take these facts very seriously. Exceptions are always there.\n Thank you for using GIRLS FACTS Alexa Skills Kit. " \
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
              "Girls like guys with sense of humor",
              "Girls hate guys who always brag about themselves",
              "It's a rare thing for girls to go for flings unlike many guys do.",
              "Take a close look at this paradox: Girls are generally impulsive buyers but are good in budgeting",
              "Too sweet girls are usually the naggers.",
              "Your girlfriend can either jokingly or seriously get jealous over your basketball games.",
              "Girls are very suspicious human beings.",
              "A guy ought understand his girl's mood swings specially when she has her monthly period.",
              "Girls love to chat about anything.",
              "Girls easily get carried away by their emotions.",
              "You must tell a girl that you are counting her. Unless you make an obvious proposal, he could either play numb or be really numb of your feelings for her.",
              "The girl who gives you a quick 'yes; could either be too impulsive.",
              "A girl's decision is always changeable.",
              "It is really hard to trace why girls are unpredictable.",
              "Girls can easily change their mind because of hearsays.",
              "Girls hate guys who gossip.",
              "You would know that a girl likes you if he laughs even at your corniest joke and even pays attention at your nonsense talk.",
              "You can hook a girl by knowing her interests.",
              "It is a fact that girls, since the birth of the world, can be professiona flirts using their magical charms.",
              "Girls hate it when you make them wait.",
              "Girls love babies.",
              "If you're truly in love with a girl, you will have a hard time to convince her telling so.",
              "Girls don't take a full meal especially when they are on a diet. But they love to eat junkfood, sweets or fruits in between meals that can double up a full meal.",
              "Beware: A girl know how to persuade you that you could do her a favor through her charisma or seductive body language without you knowing it.",
              "Girls are flattered when you make them melt in your eyes, but they would do anything just to show disapproval.",
              "Girls are very conscious people.",
              "Girls hate guys who whistle at their back. The act makes them look like cheap.",
              "Girls hate guys who hurt them physically.",
              "A girl is not necessarily after a guy towering height. He just has to be taller than she is.",
              "Girls generally do not court guys which make you guys so lucky to have their privilege to court your pick.",
              "Girls who court guys are desperate. It is awkward to see a girl courting a guy.",
              "Girls usually compete unconsciously among themselves especially when it comes to the beauty.",
              "Girls loe pampering and being pampered by their boyfriends. So be careful, this can lead her to be possessive.",
              "Never spoil a girl. Someday, if you fail to do a favor for her, she could lay the blame on you after all you did to her.",
              "Girls have changeable moods.",
              "Girls love being serenaded. The spookiest and the corniest thing that you do is for her the most romantic and the most memorable.",
              "Girls like smart guys.",
              "Girls like neat and presentable guys.",
              "If you are thinking that girls are very particular with a guy's looks, then it's time for you to make a paradigm shift. It's actually the attitude and the way you treat them that they mostly fall for.",
              "Girls can keep their deepest darkest secrets for a lifetime unlike the guys who are very open about themselves.",
              "You should let her cool first before you say sorry, otherwise she won't accept your apology.",
              "Girls usually go for older guys.",
              "Like Eve, a girl is man's weakness.",
              "Girls are generally pitiful and merciful.",
              "Girls are physically weaker than guys but are emotionally stronger when problem arise.",
              "Girls easily cry. That is why they are rarely violent because they ventilate themselves through crying.",
              "A girl smokes and drinks though she knows it's not a good impression on her.",
              "Girls love gentleman.",
              "Girls like guys who can protect and defend them. You don't have to be a macho man though.",
              "Girls hate weaklings. It's enough that their gender has the weakest physique of all human being.",
              "A girl can be fond of an effeminate. They may fall in love with a gay under considerable reasons.",
              "Girls are constantly demure when guys ( especially their crushes ) are around but can be wild behind their  back.",
              "A girl hates it when her friend squeals about her crushes or secrets.",
              "A girl that admired a stranger could research even the least and nonsense bits of info about him.",
              "Girls are generally more organized people than guys.",
              "Girls wear makeup not because they are not confident with how they look because they want to highlight their physical assets.",
              "Girls like guys with electrical and carpentering skills. These assure them that they can handle even the smallest and the peculiar thing.",
              "Girls like McGyver-like guys who can easily look for a way out when situations corner them.",
              "Girls are generally good in subjects like Language and Social Science than Mathematics and General Science.",
              "If a girl says 'no',believe her. If a girl really likes you, she wouldn't give you a 'no'. She'll give you hanging messages instead.",
              "Girls can play hard-to-get when they think her crush or suitor finds her obvious that she has feelings for him.",
              "Girls have legions of insecurities.",
              "Girls also stammer when they're talking to the guy they truly admire.",
              "Girls have innumerable crushes but her heart belongs to only to one guy.",
              "Girls mature faster and grow older than guys their same age.",    
              "Girls are more prone to getting fat easily.",
              "Girls love receiving letters.",
              "Girls are mostly panic-buyers and worriers.",
              "Girls love surprises.",
              "It is false humility girls show when they are given compliments.",
              "It is by playing tame pussycat but you tame the shrew.",
              "Before you court a girl, study her inside out.",
              "Girls are particular in getting, grouping, or having things in one color.",
              "It's hard for a girl to recover from her past.",
              "A girls prefers to learn about relationships from novels than through experience.",
              "A girl can easily forgive you if you are sincere with your apology.",
              "A girl can only be healed from her past through the enabling touch of God.",
              "Girls murmur a lot or make tantrums when they get irritated. They can control their emotions but not their temper.",
              "Girls easiy get watery eyed over telenovelas and dramas.",
              "A girl gets annoyed to a guy who pushes himself so hard to get her.",
              "Girls act snob to guys either they like too much or hate too much.",
              "A girl can suppress her feelings if she knows that a relationship wouldn't work.",
              "Girls are weight conscious.",
              "If a guy ia too innocent about handling a relationship, a girl would rather dump him.",
              "Girls love being wooed.",
              "A girl would flaunt her assets just to hook you.",
              "Immature guys are out from girl's list.",
              "Girls drool a lot over shopping malls.",
              "Girls like guys with broad shoulders and chests.",
              "Girls admire sports minded guys a lot.",
              "High heels increase a girl's poise on a catwalk.",
              "Girls love guys who can bear with what they feel.",
              "Girls are genetically sensitive.",
              "Unless a girl enters Nursing, Biology, or Medical courses or profession, she will always have that irk from seeing blood and wil always repel to see, smell, or even hear disgusting stuff.",
              "A girl loves talking all alone with the guy she's truly in love with especially in romantic and isolated places.",
              "It is not always because she said 'yes' that she likes or loves you. She could have just said it for superficial reasons.",
              "A girl can make you wait for years in courting her but could eventually give you a 'no' in the long run.",
              "There's somehow a prick in a girl, who busted you, when she learns you are courting another girl, she'll thinks that the girl would rather dump you also." 
       ]

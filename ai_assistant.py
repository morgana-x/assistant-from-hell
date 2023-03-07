import pyttsx3
import requests
import json
import speech_recognition as sr
import random
import webbrowser


print("Speech recognition initialized!")
engine = pyttsx3.init("sapi5")
"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)



print("Text to speech initialized!")
def insult():
  print("Preparing insult....")
  x = requests.post('https://evilinsult.com/generate_insult.php?lang=en&type=json')
  d = x.json()
  print(d["insult"])
  engine.say(d["insult"])
  engine.runAndWait()
def kanye():
  print("Preparing kanye quote....")
  x = requests.get('https://api.kanye.rest/')
  d = x.json()
  print(d["quote"])
  engine.say(d["quote"])
  engine.runAndWait()
def advice():
  print("Preparing advice  quote....")
  x = requests.get('https://api.adviceslip.com/advice')
  d = x.json()
  print(d)
  print(d["slip"]["advice"])
  engine.say(d["slip"]["advice"])
  engine.runAndWait()
def create_meme_imgflip(template,caption1, caption2):
  j = {
    "template_id" : template,
    "username" : "",
    "password" : "",
    "text0" : caption1,
    "text1" : caption2,
    
  }

def weather():
  print("Preparing weather....")
  x = requests.get('https://animechan.vercel.app/api/random')
  d = x.json()  
def anime_quote():
  print("Preparing anime  quote....")
  x = requests.get('https://animechan.vercel.app/api/random')
  d = x.json()
  print(d)
  if 'error' in d:
    print(d["error"])
    sayText(d["error"])
    return
  quote = d["quote"]
  anime = d["anime"]
  char = d["character"]
  phrase = "In " + anime + ", " + char + " said, " + quote
  print(phrase)
  engine.say(phrase)
  engine.runAndWait()
def catbody_image():
  print("Preparing catboy image....")
  re = "https://api.catboys.com/img"
  x = requests.get(re)
  d = x.json()
  print(d)
  if ('error' in d) and d["error"] != "none":
    print(d["error"])
    sayText(d["error"])
    return
  url = d["url"]
  sayText("I have found a catboy image")
  webbrowser.open(url, new=2)

def catboy_say():
  print("Preparing catboy saying....")
  re = "https://api.catboys.com/catboy"
  x = requests.get(re)
  d = x.json()
  print(d)
  if ('error' in d) and d["error"] != "none":
    print(d["error"])
    sayText(d["error"])
    return
  response = d["response"]
  sayText(response)
def random_fact():
  print("Random fact")
  re = 'https://uselessfacts.jsph.pl/api/v2/facts/random'
  x = requests.get(re)
  d = x.json()
  print(d)
  if ('error' in d) and d["error"] != "none":
    print(d["error"])
    sayText(d["error"])
    return
  fact = d["text"]
  print(fact)
  engine.say(fact)
  engine.runAndWait() 
def anime_quote_title(title):
  print("Preparing anime  quote....")
  re = 'https://animechan.vercel.app/api/random/anime?title=' + title
  x = requests.get(re)
  d = x.json()
  print(d)
  if ('error' in d) and d["error"] != "none":
    print(d["error"])
    sayText(d["error"])
    return
  quote = d["quote"]
  anime = d["anime"]
  char = d["character"]
  phrase = "In " + anime + ", " + char + " said, " + quote
  print(phrase)
  engine.say(phrase)
  engine.runAndWait()
def anime_quote_character(title):
  print("Preparing anime  quote....")
  re = 'https://animechan.vercel.app/api/random/character?name=' + title
  x = requests.get(re)
  d = x.json()
  print(d)
  if ('error' in d) and d["error"] != "none":
    print(d["error"])
    sayText(d["error"])
    return
  quote = d["quote"]
  anime = d["anime"]
  char = d["character"]
  phrase = "In " + anime + ", " + char + " said, " + quote
  print(phrase)
  engine.say(phrase)
  engine.runAndWait()
def sayText(text):
  engine.say(text)
  engine.runAndWait()
#kanye()
#advice()

#commands = getCommands()
def processCommand(assumed_text):
      assumed_text = assumed_text.lower()
      print(assumed_text)
      if assumed_text.find("insult") != -1:
        print("Detected the word insult!")
        insult()
        return
      if assumed_text.find("advice") != -1:
        advice()
        return
      if assumed_text.find("joke") != -1:
        print("Detected the word joke!")
        sayText("The only joke I know is you.")
        return
      if assumed_text.find("what is this") != -1:
        insult()
        return
      if assumed_text.find("make me feel better") != -1:
        insult()
        return
      if assumed_text.find("meme") != -1 and assumed_text.find("create") != -1:
        print("Creating image flip meme")
        args = assumed_text.split(" ")
        if len(args) > 3:
          create_meme_imgflip(181913649,args[2], args[3])
      if ( (assumed_text.find("catboy") != -1 or assumed_text.find("cat boy") != -1) ) and (assumed_text.find("find") != -1 or assumed_text.find("random") != -1 or assumed_text.find("get") != -1) and assumed_text.find("image") != -1:
        catbody_image()
        return
      if ( (assumed_text.find("catboy") != -1 or assumed_text.find("cat boy") != -1) ) and (assumed_text.find("find") != -1 or assumed_text.find("say") != -1 or assumed_text.find("random") != -1 or assumed_text.find("get") != -1) and (assumed_text.find("quote") != -1 or assumed_text.find("saying") != -1):
        catboy_say()
        return
      if assumed_text.find("anime") != -1:
        if assumed_text.find("quote") != -1:
           if assumed_text.find("from") != -1:
              args = assumed_text.split(" ")
              title = args[len(args)-1]
              print(title)
              if title and len(title) > 2:
                print(title + " is valid")
                anime_quote_title(title)
                return
           if assumed_text.find("by") != -1:
              args = assumed_text.split(" ")
              title = args[len(args)-1]
              print(title)
              if title and len(title) > 2:
                print(title + " is valid")
                anime_quote_character(title)
                return
           anime_quote()
           return
      if assumed_text.find("motivation") != -1 and assumed_text.find("give") != -1:
        insult()
        return
      if assumed_text.find("kanye") != -1 and assumed_text.find("quote") != -1:
        kanye()
        return
      if (assumed_text.find("find") != -1 or assumed_text.find("random") != -1 or assumed_text.find("get") != -1) and assumed_text.find("fact") != -1:
        random_fact()
      if assumed_text.find("tell my friend how special they are") != -1:
        insult()
        return
      if assumed_text.find("thankyou") != -1:
        sayText("No problem.")
        return
      if assumed_text.find("thank you") != -1:
        sayText("No problem.")
        return
      if assumed_text.find("weather") != -1:
        # do weather stuff
        print("Detected weather")
        return
        

def processRaw(assumed_text):
  assumed_text = assumed_text.lower()
  print("Processing " + assumed_text + "...")
  #if assumed_text.find("alexa") != -1:
  processCommand(assumed_text)

def voiceDetect_Sphinx():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
      assumed_text = r.recognize_sphinx(audio)
      print(assumed_text)
      return assumed_text, True
    except sr.UnknownValueError:
      print("Sphinx could not understand audio")
    except sr.RequestError as e:
      print("Sphinx error; {0}".format(e))
    return "", False
def voiceDetect_Whipser():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 650
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
      assumed_text = r.recognize_whisper(audio, language="english")
      print(assumed_text)
      return assumed_text, True
    except sr.UnknownValueError:
      print("Whisper could not understand audio")
    except sr.RequestError as e:
      print("Could not request results from Whisper")
    return "", False
def voiceDetect_Google():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    r.energy_threshold = 1000
    #r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
  try:
    assumed_text = r.recognize_google(audio)
    return assumed_text, True
  except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
  except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
  return "", False
randomSorry = ["Sorry I could not recognise that", "What are you saying", "I can't understand you", "You speak in gibberish not english", "I am programmed to listen to intelligent speech, you clearly aren't capable of that"]
while True:
    print("waiting")
    assumed_text, success = voiceDetect_Google()
    
    print("Got text")
    if success:
      processRaw(assumed_text)
    #else:
     # sayText(random.choice(randomSorry))

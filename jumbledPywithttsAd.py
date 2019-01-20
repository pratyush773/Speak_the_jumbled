import speech_recognition as sr
from gtts import gTTS
import os
import time


r = sr.Recognizer()
r.energy_threshold = 8000



def main():
    
    language = 'en'
    InitialText1="Welcome to Jumbled World. May I know your name"
    myobj1 = gTTS(text=InitialText1, lang=language, slow=False)
    myobj1.save("welcome1.mp3")
    os.system("welcome1.mp3")
    time.sleep(2)

    with sr.Microphone() as source:                # use the default microphone as the audio source
      audio1=r.listen(source)
      key=r.recognize_google(audio1)
      
      InitialText2="Say Something"+key
      myobj2 = gTTS(text=InitialText2, lang=language, slow=False)
      myobj2.save("welcome2.mp3")
      os.system("welcome2.mp3")

    with sr.Microphone() as source:
            
      audio2 = r.listen(source)                   # listen for the first phrase and extract it into audio data
      key=r.recognize_google(audio2)
      
     # myobj5 = gTTS(text=key, lang=language, slow=False)
     # myobj5.save("welcome6.mp3")
     # os.system("welcome6.mp3")


      InitialText3="Said"
      myobj5 = gTTS(text=InitialText3, lang=language, slow=False)
      myobj5.save("welcome5.mp3")
      os.system("welcome5.mp3")
      
    
    try:
      key=r.recognize_google(audio2)
      print("You said " + key)
      fi=open('Dictionary.txt','rU')
      content=fi.read()
      #print(content)
      key=sorted(key)

      welcometext="The jumble words from the input are as follows"
      myobj3 = gTTS(text=welcometext, lang=language, slow=False)
      myobj3.save("welcome3.mp3")
      os.system("welcome3.mp3")
      time.sleep(3)
      for word in content.split():
         if(len(key) == len(word)): 
           if(key==sorted(word)):
              print(word)
              mytext = word
              myobj4 = gTTS(text=mytext, lang=language, slow=False)
              myobj4.save("welcome4.mp3")
              os.system("welcome4.mp3")
              
      fi.close()  
    except LookupError:                            # speech is unintelligible
      print("Could not understand audio")

    
    

    


if __name__=='__main__':
    main()



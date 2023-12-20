import speech_recognition as sr

def listener(language):
     r = sr.Recognizer()
     with sr.Microphone() as source:
          print("I am listening sire...")
          r.pause_threshold = 1
          audio = r.listen(source)
     languages = {"en":"en-US", "fr":"fr-FR", "kn":"kn-IN"}
     try:
          text = r.recognize_google(audio, language=languages.get(language))
          print(f"Google Speech Recognition ({language}) thinks you said:", text)
          return text
     except sr.UnknownValueError:
          print(f"Google Speech Recognition ({language}) could not understand audio")
          return None
     except sr.RequestError as e:
          print(f"Could not request results from Google Speech Recognition service ({language}); {e}")
          return None
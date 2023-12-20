import numpy as np
from listener import listener
import os
from gtts import gTTS
import time
import pandas as pd


def speak(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    filename = "temp_audio.mp3"
    tts.save(filename)
    os.system(filename) 
    time.sleep(3)
    
    
def ask_and_store(language):
    outputs = []

    questions = {
    'en': [
        "Can you tell me the crop year?",
        "How much annual rainfall was there?",
        "What season does the crop belong to?",
        "What is the name of the crop?",
        "In which state was the crop grown?"
    ],
    'fr': [
        "Pouvez-vous me dire l'année de la culture?",
        "Combien y avait-il de pluies annuelles?",
        "À quelle saison appartient la culture?",
        "Quel est le nom de la culture?",
        "Dans quel état la culture a-t-elle été cultivée?"
    ],
    'kn': [
        "ನೀವು ಬೆಳೆಗಾರನು ಎಂದು ಹೇಳಬಹುದು?",
        "ವಾರ್ಷಿಕ ಮಳೆ ಎಷ್ಟು ಇತ್ತು?",
        "ಬೆಳೆಗಾರ ಯಾವ ಋತುಗೊಳಿಸಲಾಯಿತು?",
        "ಬೆಳೆಗಾರದ ಹೆಸರೇನು?",
        "ಬೆಳೆಗಾರ ಯಾವ ರಾಜ್ಯದಲ್ಲಿ ಬೆಳೆಯಲ್ಪಟ್ಟಿತು?"
    ]
    }   

    lang_questions = questions.get(language, [])

    for question in lang_questions:
        speak(question, language=language)
        output = listener(language) 
        outputs.append(output) 
        
    outputs = pd.DataFrame([outputs],
                         columns=['Crop_Year', 'Annual_rainfall', 'Season', 'Crop', 'state'])

    return outputs


from gtts import gTTS
import os

def audio_response(normalized_input, language='en'):
    """
    Generate audio response for the given input and language.

    Parameters:
    - normalized_input (str): The input to be spoken.
    - language (str): Language of the input ('en', 'fr', or 'kn').

    Returns:
    - None
    """
    
    if language == 'en':
        tts = gTTS(text=f"The predicted yield of the crop for given conditions is: {normalized_input}", lang='en', slow=False)
    elif language == 'fr':
        tts = gTTS(text=f"La production prévue de la culture pour les conditions données est : {normalized_input}", lang='fr', slow=False)
    elif language == 'kn':
        tts = gTTS(text=f"ನೀಡಿದ ಸ್ಥಿತಿಗಾಗಿ ಹೊರಗಿನ ಪೈಲಾನೆನ್ನು ಅನುಮಾನಿಸಲಾಗಿದೆ: {normalized_input}", lang='kn', slow=False)
    else:
        tts = gTTS(text=f"The predicted yield of the crop for given conditions is: {normalized_input}", lang='en', slow=False)

    tts.save("temp_output.mp3")
    
    os.system("temp_output.mp3") 

    os.remove("temp_ouput.mp3")



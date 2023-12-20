import pickle
import pandas as pd
from talker import audio_response

encoder_path = 'models/encoder.pkl'

input_df = pd.DataFrame([[1997, 2051.4, "Rabi       ", 'Jute', "Gujarat"]],
                         columns=['Crop_Year', 'Annual_Rainfall', 'Season', 'Crop', 'state'])


with open(encoder_path, 'rb') as encoder_file:
    encoder = pickle.load(encoder_file)
    
    cat_features = ['Season', 'Crop', 'state']
    
    encoded_data = encoder.transform(input_df[cat_features])
    
    data = input_df.join(encoded_data.add_suffix("_count"))
    data = data.drop(columns=cat_features)
    
    data = input_df.join(encoded_data.add_suffix("_count"))
    data = data.drop(columns=cat_features)
    
    with open('models/model.pkl', 'rb') as model_file:
        loaded_model = pickle.load(model_file)
    
    predictions = loaded_model.predict(data)
    
print(predictions)

audio_response(predictions)

print(data)
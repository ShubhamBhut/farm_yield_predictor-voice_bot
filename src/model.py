import category_encoders as ce
import pandas as pd
import pickle

def predict_with_encoder(input_df, model_path='models/model.pkl', encoder_path='models/encoder.pkl'):
    """
    Make predictions using a pre-trained model and encoder.

    Parameters:
    - input_df (DataFrame): Input data to be encoded and predicted.
    - model_path (str): Path to the saved model file.
    - encoder_path (str): Path to the saved encoder file.

    Returns:
    - predictions (ndarray): Predictions made by the model.
    """
    
    with open(encoder_path, 'rb') as encoder_file:
        encoder = pickle.load(encoder_file)
    
    cat_features = ['Season', 'Crop', 'state']
    
    encoded_data = encoder.transform(input_df[cat_features])
    
    data = input_df.join(encoded_data.add_suffix("_count"))
    data = data.drop(columns=cat_features)
    
    with open(model_path, 'rb') as model_file:
        loaded_model = pickle.load(model_file)
    
    predictions = loaded_model.predict(data)
    
    return predictions

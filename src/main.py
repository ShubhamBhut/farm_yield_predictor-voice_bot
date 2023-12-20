from talker import ask_and_store, audio_response
from model import predict_with_encoder

input_data = ask_and_store("en")
print(input_data)
print(type(input_data))

prediction = predict_with_encoder(input_data)

audio_response(prediction)
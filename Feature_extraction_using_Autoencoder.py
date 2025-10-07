from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
import numpy as np

# Define the autoencoder model
input_dim = df['content'].apply(len).max()  # Max length of content
input_layer = Input(shape=(input_dim, ))
encoder = Dense(128, activation="relu")(input_layer)
encoder = Dense(64, activation="relu")(encoder)
encoder = Dense(32, activation="relu")(encoder)
encoder_output = Dense(16, activation="relu")(encoder)

decoder = Dense(32, activation="relu")(encoder_output)
decoder = Dense(64, activation="relu")(decoder)
decoder = Dense(128, activation="relu")(decoder)
output_layer = Dense(input_dim, activation="sigmoid")(decoder)

autoencoder = Model(inputs=input_layer, outputs=output_layer)
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

# Prepare data for autoencoder
def pad_data(data, max_len):
    return np.array([np.pad(d, (0, max_len - len(d)), 'constant') for d in data])

content_data = df['content'].apply(lambda x: np.frombuffer(x.encode(), dtype=np.uint8)).tolist()
content_data = pad_data(content_data, input_dim)

# Train the autoencoder
autoencoder.fit(content_data, content_data, epochs=50, batch_size=256, shuffle=True)

# Extract features
encoder_model = Model(inputs=input_layer, outputs=encoder_output)
features = encoder_model.predict(content_data)

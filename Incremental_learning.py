def update_model(new_data):
    # Prepare new data
    new_content_data = new_data['content'].apply(lambda x: np.frombuffer(x.encode(), dtype=np.uint8)).tolist()
    new_content_data = pad_data(new_content_data, input_dim)
    
    # Train the autoencoder on new data
    autoencoder.fit(new_content_data, new_content_data, epochs=10, batch_size=256, shuffle=True)
    
    # Extract new features
    new_features = encoder_model.predict(new_content_data)
    
    return new_features

# Simulate new data arrival
new_data = pd.DataFrame({
    'file_id': ['new_file1', 'new_file2'],
    'content': ['new content 1', 'new content 2']
})

new_features = update_model(new_data)

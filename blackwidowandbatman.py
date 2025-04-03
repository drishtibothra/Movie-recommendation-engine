def classification():
    import streamlit as st
    from keras.models import Sequential
    from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
    from keras.preprocessing import image
    import numpy as np
    from PIL import Image

    # Function to create and compile the CNN model
    def create_model():
        model = Sequential()
        model.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Conv2D(32, (3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Flatten())
        model.add(Dense(units=128, activation='relu'))
        model.add(Dense(units=1, activation='sigmoid'))
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    # Load or create the model
    classifier = create_model()

    # Streamlit app layout
    st.title("Black Widow vs Batman Identifier")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image to classify", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display uploaded image
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)

        # Preprocess the image
        img = img.resize((64, 64))  # Resize the image to the required size for the model
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)  # Expand dims to fit model input shape

        # Predict
        result = classifier.predict(img_array)
        prediction = "Black Widow" if result[0][0] > 0.5 else "Batman"

        # Display prediction
        st.write(f"Prediction: {prediction}")

classification()

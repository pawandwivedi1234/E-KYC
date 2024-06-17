# E-KYC Project
Welcome to the E-KYC project! This project leverages cutting-edge techniques in computer vision, natural language processing, convolutional neural networks (CNNs), and long short-term memory networks (LSTMs) to facilitate automatic Know Your Customer (KYC) processes. 

## Overview

The E-KYC web application provides an interactive user interface where users can upload their ID card (limited to Aadhar and PAN cards at the moment) and a photograph of their face. The app then internally processes the provided ID card to extract the face and matches it with the uploaded photograph. 

### Features

1. **Face Verification**: The app computes the face from the provided ID card using Haarcascade and matches it with the uploaded photograph. If the verification status is successful, subsequent operations are carried out; otherwise, an error is generated.
   
## Face Verification Demo

![E-KYC-FACE VERIFICATION DEMO](https://github.com/abhishekiiitbh2903/E-KYC-/blob/main/assets/ekyc%20face%20verification.gif)


Herein, I have uploaded an ID card of my dad and an image of myself. As a result, the face verification fails, and as stated above, the subsequent codes do not execute.

2. **Optical Character Recognition (OCR)**: If face verification is successful, the app uses EasyOCR with a predefined threshold value to extract text from the ID card.
3. **Database Interaction**: The extracted text and face embeddings are checked for duplicacy before being inserted into the database. If the user is already registered, the SQL query is not executed, and the fetched result is returned.
4. **Face Embeddings**: The app uses FaceNet from DeepFace to retrieve face embeddings, which are also stored in the database.

### Technologies Used

- **Computer Vision**: For face detection and verification.
- **Natural Language Processing**: For text extraction and processing.
- **Convolutional Neural Networks (CNNs)**: For image processing tasks.
- **Long Short-Term Memory Networks (LSTMs)**: For handling sequential data.
- **EasyOCR**: For OCR operations.
- **DeepFace**: For face embeddings.
- **Haarcascade**: For detecting faces in ID cards.

## Upcoming Improvements

1. **Live Face Detection**: Instead of taking a face image from the user, the app will detect the face image live using the device's camera.
2. **Data Privacy**: Currently, original values are stored in the database. In future updates, sensitive data (like original IDs) will be hashed before storage to ensure privacy even if the database is compromised.

## Logging

Proper logging has been maintained throughout the project to facilitate easier debugging and monitoring.

## Author

This project is authored by Abhishek Singh, a final year B.Tech CSE undergraduate at IIIT Bhubaneswar. You can reach me at abhishekrathore1806@gmail.com.

## Contributing

I am open to contributions! If you can work on the possible areas of improvement or have other enhancements in mind, feel free to fork the repository, make your changes, and initiate a pull request. If the changes are legitimate and add value to the project, I will merge them.

Happy coding! 😊

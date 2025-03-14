# AI Medical Chatbot

## Overview
The AI Medical Chatbot is an interactive application that leverages artificial intelligence to assist users with medical inquiries. It utilizes audio and image inputs to provide responses that mimic a professional doctor's advice.

## Features
- **Voice Interaction**: Users can record their queries, which are transcribed into text.
- **Image Analysis**: Users can upload medical images for analysis, and the chatbot provides insights based on the content of the images.
- **Text-to-Speech**: Responses from the chatbot are converted into speech, allowing for a seamless interaction experience.

## Project Structure
```
ai-medical-chatbot
├── app
│   ├── gradio_app.py         # Main application logic for the Gradio interface
│   ├── brain_of_doc.py       # Functions for analyzing medical images
│   ├── voice_of_patient.py    # Functions for recording and transcribing audio
│   ├── voice_of_doc.py       # Functions for text-to-speech conversion
│   └── utils.py              # Utility functions used across the application
├── static
│   └── temp_audio            # Directory for storing temporary audio files
├── requirements.txt          # Python dependencies for the project
├── Dockerfile                # Instructions to build a Docker image
├── docker-compose.yml        # Configuration for multi-container Docker applications
├── .env.example              # Template for environment variables
└── README.md                 # Documentation for the project
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd ai-medical-chatbot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Copy `.env.example` to `.env` and fill in the necessary values.

## Running the Application
To run the application locally, execute the following command:
```
python app/gradio_app.py
```
This will start the Gradio interface, which can be accessed at `http://127.0.0.1:7860`.

## Docker Deployment
To deploy the application using Docker, run:
```
docker-compose up --build
```
This command will build the Docker image and start the application in a container.

## Usage
- Record your voice query using the microphone input.
- Upload a medical image for analysis.
- The chatbot will provide a response based on the audio and image inputs.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
def text_to_speech_with_gtts(input_text, output_filepath):
    from gtts import gTTS
    import os

    tts = gTTS(text=input_text, lang='en')
    tts.save(output_filepath)
    return output_filepath


def text_to_speech_with_elevenlabs(input_text, output_filepath):
    import requests

    api_key = os.environ.get("ELEVEN_LABS_API_KEY")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "text": input_text,
        "voice": "en_us_male",  # Example voice, adjust as needed
        "output_format": "mp3"
    }
    
    response = requests.post("https://api.elevenlabs.io/v1/text-to-speech", headers=headers, json=data)

    if response.status_code == 200:
        with open(output_filepath, 'wb') as audio_file:
            audio_file.write(response.content)
        return output_filepath
    else:
        raise Exception("Error in text-to-speech conversion: " + response.text)
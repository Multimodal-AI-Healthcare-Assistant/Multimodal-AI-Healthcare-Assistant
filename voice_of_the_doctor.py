# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

#Step1a: Setup Text to Speech–TTS–model with gTTS
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


input_text="Hi This is Atharva Raut. owner of RCOEM!"
#text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

#Step1b: Setup Text to Speech–TTS–model with ElevenLabs (UPDATED)
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")  # Changed from ELEVEN_API_KEY

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    if not ELEVENLABS_API_KEY:
        print("Error: ELEVENLABS_API_KEY not found in environment variables")
        return
    
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    
    # Use the new text_to_speech.convert() method with correct voice ID
    audio = client.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB",  # Adam voice ID (reliable)
        output_format="mp3_44100_128",
        text=input_text,
        model_id="eleven_turbo_v2"
    )
    
    # Save the audio
    with open(output_filepath, "wb") as f:
        for chunk in audio:
            f.write(chunk)
    print(f"Audio saved to {output_filepath}")

#text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3")

'''


    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


input_text="Hi this is atharva raut!"
text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

#Step1b: Setup Text to Speech–TTS–model with ElevenLabs
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY=os.environ.get("ELEVEN_API_KEY")

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "Aria",
        output_format= "mp3_44100_128",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3") 
'''
#Step2: Use Model for Text output to Voice

import subprocess
import platform

def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            #subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
            subprocess.run(['powershell', '-c', f'Start-Process "{output_filepath}"'], check=True)
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


input_text="Hi this is Atharva raut, autoplaytesting it is! with gTTS model."
text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.wav")


import subprocess
import platform
from elevenlabs.client import ElevenLabs

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    
    # Use the new text_to_speech.convert() method
    audio = client.text_to_speech.convert(
        voice_id="TC0Zp7WVFzhA8zpTlRqV",  # Aria voice ID
        output_format="mp3_22050_32",
        text=input_text,
        model_id="eleven_turbo_v2"
    )
    
    # Save the audio using chunks
    with open(output_filepath, "wb") as f:
        for chunk in audio:
            f.write(chunk)
    
    # Autoplay the audio
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            # Use Start-Process for MP3 files (fixed from your gTTS solution)
            subprocess.run(['powershell', '-c', f'Start-Process "{output_filepath}"'], check=True)
        elif os_name == "Linux":  # Linux
            subprocess.run(['mpg123', output_filepath])  # Use mpg123 for MP3
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

#text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")





















'''

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")
'''
'''


# ---------------------------------------------------------
# Step 1a: Setup Text-to-Speech (TTS) using Google Text-to-Speech (gTTS)
# ---------------------------------------------------------

# gTTS (Google Text-to-Speech) is a Python library that connects to Google's TTS API
# It takes text as input, processes it, and outputs an audio file in various formats (e.g., MP3).
# This block converts the given `input_text` into an audio file using the specified `language`.

from gtts import gTTS  # Import Google Text-to-Speech library

# Function to convert text into speech using gTTS
# Parameters:
#   input_text: The text string to be converted to audio
#   language: Language code (e.g., "en" for English)
#   slow: Boolean value to control speech speed (False = normal speed, True = slow speech)
#   output_filepath: File path where the generated audio will be saved
audioobj = gTTS(
    text=input_text,      # Text to be converted into audio
    lang=language,        # Language of the speech (e.g., 'en')
    slow=False            # Speech speed (False for normal speed)
)

# Save the generated speech audio to a file
audioobj.save(output_filepath)

# Example usage of the gTTS function
input_text = "Hi this is Atharva Raut!"
text_to_speech_with_gtts_old(
    input_text=input_text,
    output_filepath="gtts_testing.mp3"  # MP3 file will be saved in the working directory
)


# ---------------------------------------------------------
# Step 1b: Setup Text-to-Speech (TTS) using ElevenLabs API
# ---------------------------------------------------------

# ElevenLabs provides a high-quality, AI-powered speech synthesis API.
# It allows you to select voices, set speech speed, control format, and generate more natural-sounding audio than many basic TTS systems.
# This code uses the ElevenLabs Python client to connect to their API and generate speech.

import os
import elevenlabs
from elevenlabs.client import ElevenLabs  # Import the ElevenLabs API client

# Retrieve ElevenLabs API Key from environment variables
# IMPORTANT: Ensure you have set the environment variable ELEVEN_API_KEY before running the code
ELEVENLABS_API_KEY = os.environ.get("ELEVEN_API_KEY")

# Function to convert text into speech using ElevenLabs API
# Parameters:
#   input_text: The text to convert into audio
#   output_filepath: The destination file path where the generated audio will be saved
# This function uses the "Aria" voice, outputs an MP3 file at 44.1 kHz, and uses the `eleven_turbo_v2` model.
def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    # Create an ElevenLabs client instance with the provided API key
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    
    # Generate audio from text
    # Parameters:
    #   text: The input text to synthesize
    #   voice: Predefined voice ID or name (e.g., "Aria")
    #   output_format: Audio format (sample rate, bitrate)
    #   model: The TTS model version to use
    audio = client.generate(
        text=input_text,
        voice="Aria",                     # Voice name from ElevenLabs voice library
        output_format="mp3_44100_128",    # MP3, 44.1 kHz, 128 kbps
        model="eleven_turbo_v2"           # High-speed, high-quality TTS model
    )
    
    # Save the generated audio to the specified file path
    elevenlabs.save(audio, output_filepath)

# Example usage of the ElevenLabs TTS function
text_to_speech_with_elevenlabs_old(
    input_text=input_text,
    output_filepath="elevenlabs_testing.mp3"  # MP3 file will be saved in the working directory
)
'''

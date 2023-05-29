# Personal-Assistant
As we know Python is a suitable language for scriptwriters and developers. Let’s write a script for Voice Assistant using Python. This project was developed to overcome high CPU usage of Cortana in Windows 10 and also providing a assistant to the lower versions of Windows which did not have feature like Cortana.

## Personal Assistant Using Python.py File

This code represents a Personal Assistant called LARVIS (acronym for "Life Assistance and Response Virtual Intelligent System"). It allows users to interact with the assistant using voice commands to perform various tasks such as opening web pages, sending emails, retrieving information from the web, playing music, and more.

The code is written in Python and utilizes several libraries and APIs to enable different functionalities. Here's a brief overview of the key components:

### Libraries Used
- `pyttsx3`: Library for text-to-speech synthesis.
  Syntax to install library:
  
  ```
  pip install pyttsx3
  ```
- `webbrowser`: Library for web browsing functionality.
  Syntax to install library:
  
  ```
  pip install webbrowser
  ```
- `smtplib`: Library for sending emails.
  Syntax to install library:
  
  ```
  pip install smtplib
  ```
- `random`: Library for generating random numbers and values.
  Syntax to install library:
 
 ```
  pip install random
  ```
- `speech_recognition`: Library for speech recognition.
  Syntax to install library:
  
  ```
  pip install SpeechRecognition
  ```
- `wikipedia`: Library for querying information from Wikipedia.
  Syntax to install library:
  
  ```
  pip install wikipedia
  ```
- `datetime`: Library for working with dates and times.
  Syntax to install library:
  
  ```
  pip install datetime
  ```
- `wolframalpha`: Library for accessing the Wolfram|Alpha computational knowledge engine.
  Syntax to install library:
  
  ```
  pip install wolframalpha
  ```
- `os`: Library for interacting with the operating system.
  Syntax to install library:
  
  ```
  pip install os
  ```
- `sys`: Library for system-specific parameters and functions.
  Syntax to install library:
  
  ```
  pip install sys
  ```
- `playsound`: Library for playing sound files.
  Syntax to install library:
  
  ```
  pip install playsound
  ```
- `yagmail`: Library for sending emails using Gmail.
  Syntax to install library:
  
  ```
  pip install yagmail
  ```
- `pygame`: Library for game development and multimedia applications.
  Syntax to install library:
  
  ```
  pip install pygame
  ```

### Functionality
1. **Text-to-Speech**: The `pyttsx3` library is used to convert text into speech. The assistant speaks out the responses or prompts to the user's commands.

2. **Wolfram|Alpha Integration**: The assistant can access the Wolfram|Alpha computational knowledge engine using the `wolframalpha` library. It can provide answers to queries using this powerful API.

3. **Speech Recognition**: The `speech_recognition` library enables the assistant to recognize and convert speech input into text. The assistant listens to the user's voice commands and processes them accordingly.

4. **Web Browsing**: The `webbrowser` library is used to open web pages. The assistant can open YouTube, Google, Gmail, and perform web searches based on the user's commands.

5. **Email Sending**: The `smtplib` and `yagmail` libraries enable the assistant to send emails. Users can dictate the recipient and content of the email, and the assistant automates the sending process.

6. **Music Playback**: The `pygame` library is used to play random music files from a specified folder. The assistant can start playing music and stop it when requested.

7. **Wikipedia Integration**: The `wikipedia` library allows the assistant to retrieve information from Wikipedia. It can provide summaries for specific queries.

8. **Greeting and Conversation**: The assistant greets the user based on the current time and engages in basic conversation, responding to general greetings or questions.

### Usage
To use the personal assistant, you can run the code in a Python environment, such as Jupyter Notebook or a command-line interface. The assistant listens for voice commands, processes them, and performs the requested tasks accordingly.

Please note that some functionalities, such as email sending or music playback, may require additional configurations or specific paths to be set within the code.

Feel free to explore and modify the code to customize the assistant's behavior and add more functionalities as per your requirements.

**Note:** Remember to replace `'YOUR_APP_ID'` and `'PLEASE_ENTER_YOUR_MUSIC_FOLDER_PATH'` with your own values or paths as indicated in the code comments.

Have fun experimenting with your voice-controlled personal assistant, LARVIS!

## Personal-Assistant-Music-Library

Each line represents a separate MP3 file with its corresponding filename. Here's a breakdown of the files mentioned:

- "AS IF IT'S YOUR LAST" by BLACKPINK: A song by the South Korean girl group BLACKPINK.
- "Agar Tum Saath Ho": A song from the Bollywood movie "Tamasha".
- "Baby": A song by Justin Bieber.
- "Enna Sona": A song from the Bollywood movie "Ok Jaanu".
- "Halka Halka": A song from the Bollywood movie "Fanney Khan".
- "Hamdard": A song from the Bollywood movie "Ek Villain".
- "Hawayein": A song from the Bollywood movie "Jab Harry Met Sejal".
- "Ishq Wala Love": A song from the Bollywood movie "Student of the Year".
- "Jab Tak": A song from the Bollywood movie "M.S. Dhoni: The Untold Story".
- "Kaise Hua": A song from the Bollywood movie "Kabir Singh".
- "Kesariya": A song from the Bollywood movie "Kesari".
- "Maan Meri Jaan": A song from the Bollywood movie "Manmarziyaan".
- "Main Dhoondne Ko Zamaane Mein": A song from the Bollywood movie "Heartless".
- "Mann Mera": A song from the Bollywood movie "Table No. 21".
- "Mast Magan": A song from the Bollywood movie "2 States".
- "Raabta": A song from the Bollywood movie "Agent Vinod".
- "Shayad": A song from the Bollywood movie "Love Aaj Kal".
- "Tera Hone Laga Hoon": A song from the Bollywood movie "Ajab Prem Ki Ghazab Kahani".
- "Tera Yaar Hoon Main": A song from the Bollywood movie "Sonu Ke Titu Ki Sweety".
- "Tu Aake Dekhle": A song from the Bollywood movie "Mumbai Mirror".

## Software Requirements
Operating System (OS): Windows 7 and Above (64-bit)
RAM: 4GB or more
Graphics Card: N/A
Processor: Intel i3 or Above

## How To Run the project
1. You need to install [python 3.8.0](https://www.python.org/downloads/release/python-380/)
2. After installing the python IDLE open Command Prompt (CMD) on the device
3. Check for the python version installed to verify Python is successfully installed.
  
  ```
  python -version
  ```
  
4. Using the code snippets given in the [Libraries Used](#libraries-used) install each and every library in the IDLE.
5. Copy the the code in the IDLE
6. To run the code press F5 key in IDLE. 

# Jarvis AI Python Project

This is a simple AI assistant program written in Python that performs various tasks based on voice commands.

## Setup

### Windows

1. **Install Required Packages:**
   - Open a command prompt in the project directory.
   - Run the following command to install the required Python packages:

     ```bash
     pip install pyttsx3 speechrecognition wikipedia
     ```

2. **Install espeak:**
   - Download and install the espeak installer for Windows from [here](http://espeak.sourceforge.net/download.html).

3. **Run the Program:**
   - Open a command prompt in the project directory.
   - Run the program using the following command:

     ```bash
     python jarvis.py
     ```

### Linux

1. **Install Required Packages:**
   - Open a terminal in the project directory.
   - Run the following command to install the required Python packages:

     ```bash
     pip install pyttsx3 speechrecognition wikipedia
     ```

2. **Install espeak:**
   - Install espeak using the package manager. For example, on Ubuntu:

     ```bash
     sudo apt-get install espeak
     ```

3. **Install PortAudio Development Files:**
   - Install the PortAudio development files:

     ```bash
     sudo apt-get install portaudio19-dev
     ```

4. **Install pyaudio:**
   - Run the following command to install 'pyaudio':

     ```bash
     pip install pyaudio
     ```

5. **Run the Program:**
   - Open a terminal in the project directory.
   - Run the program using the following command:

     ```bash
     python jarvis.py
     ```

## Usage

- Once the program is running, Jarvis will greet you and listen for voice commands.
- Speak commands such as "Wikipedia [query]," "Open YouTube," "Play Music," "What's the time," etc.
- To exit the program, say "close" and Jarvis will say goodbye and terminate.

Feel free to customize the code and add more functionalities to enhance the capabilities of your AI assistant!

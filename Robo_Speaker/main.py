import pyttsx3
from colorama import init, Fore, Style
import time
import os

# Initialize colorama
init(autoreset=True)

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Clear the terminal screen
os.system('cls' if os.name == 'nt' else 'clear')

# Welcome message
print(Fore.CYAN + Style.BRIGHT + "="*50)
print(Fore.GREEN + Style.BRIGHT + "🤖  Welcome to ROBO Speaker 1.1")
print(Fore.YELLOW + "🔊  Created with ❤️  by Hammad Mustafa")
print(Fore.CYAN + Style.BRIGHT + "="*50)

while True:
    print()
    user_input = input(Fore.MAGENTA + "📝 Enter text to speak (or 'q' to quit): ").strip()
    
    if user_input.lower() == 'q':
        print(Fore.RED + "👋 Exiting Robo Speaker... Goodbye friend!")
        engine.say("Bye bye friend!")
        engine.runAndWait()
        break
    elif user_input == "":
        print(Fore.LIGHTRED_EX + "⚠️  You didn't type anything. Try again.")
    else:
        print(Fore.LIGHTBLUE_EX + "🎤 Speaking: " + Fore.WHITE + user_input)
        engine.say(user_input)
        engine.runAndWait()
































# import pyttsx3

# engine = pyttsx3.init()

# print("Welcome to ROBO Speaker 1.1 Created by Hammad Mustafa")

# while True:
#     user_input = input("Enter what you want me to speak (or 'q' to quit): ").strip()
#     if user_input.lower() == 'q':
#         engine.say("Bye bye friend!")
#         engine.runAndWait()
#         break
#     else:
#         engine.say(user_input)
#         engine.runAndWait()

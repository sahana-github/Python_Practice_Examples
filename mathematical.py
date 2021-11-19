import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# Program make a simple calculator
# This function adds two numbers


def add(x, y):
    return x + y
# This function subtracts two numbers


def subtract(x, y):
    return x-y
# This function multiplies two numbers


def multiply(x, y):
    return x * y
# This function divides two numbers


def divide(x, y):
    return x / y


speak("What Mathematical Operation ypu want to perform?")
speak("Select operation.")
speak("For Addition select operation one")
print("1.Add")
speak("For Subraction select operation two")
print("2.Subtract")
speak("For Multiplication select operation three")
print("3.Multiply")
speak("For Division select operation four")
print("4.Divide")

print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
# Take input from the user
choice = input("Enter choice(1/2/3/4): ")
speak("Enter first number:")
num1 = float(input("Enter first number: "))
speak("Enter second number:")
num2 = float(input("Enter second number: "))
if choice == '1':
    speak("Addition of number1 and number2 is")
    speak(add)
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    speak("Subraction of number1 and number 2 is")
    speak(subtract)
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    speak("Multiplication of number1 and number 2 is")
    speak(multiply)
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    speak("Division of number1 and number 2 is")
    speak(divide)
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")

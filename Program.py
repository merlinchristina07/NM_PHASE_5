import nltk
nltk.download('punkt')
     

from langdetect import detect
from googletrans import Translator
import time
import random

translator = Translator()

# Translate to English if needed
def translate_to_english(text):
    lang = detect(text)
    if lang != 'en':
        translated = translator.translate(text, dest='en')
        return translated.text, lang
    return text, 'en'

# Translate back to user's language
def translate_from_english(text, lang_code):
    if lang_code != 'en':
        translated = translator.translate(text, dest=lang_code)
        return translated.text
    return text

# Symptom checker logic
def symptom_checker(symptom_input):
    conditions = {
        "fever": "Possible causes: Flu, COVID-19, or infection.",
        "cough": "Possible causes: Cold, Flu, or Bronchitis.",
        "chest pain": "Possible causes: Heart condition or acid reflux.",
        "fatigue": "Possible causes: Anemia, thyroid issues, or lack of sleep."
    }
    for key in conditions:
        if key in symptom_input.lower():
            return conditions[key]
    return "Condition unclear. Recommend clinical diagnosis."

# IoT health data simulator
def iot_monitoring():
    return {
        "heart_rate": random.randint(60, 120),
        "blood_pressure": f"{random.randint(100, 140)}/{random.randint(60, 90)}",
        "oxygen_level": random.randint(90, 100)
    }

# Chatbot interface with translation
def chatbot_interface(user_input):
    translated_input, lang = translate_to_english(user_input)
    response = symptom_checker(translated_input)
    final_response = translate_from_english(response, lang)
    return final_response

# Feedback mechanism
def collect_feedback():
    try:
        rating = int(input("\nRate the system's accuracy (1–5): "))
        if rating >= 4:
            print("Thanks for the positive feedback!")
        else:
            print("We’ll work to improve the system.")
    except:
        print("Invalid rating. Skipping feedback.")

# Main interaction loop
def main():
    print("Welcome to AI Healthcare Diagnostic System")
    while True:
        print("\n1. Symptom Check")
        print("2. IoT Monitoring")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            symptoms = input("Describe your symptoms: ")
            result = chatbot_interface(symptoms)
            print("AI Response:", result)
            collect_feedback()

        elif choice == '2':
            print("Real-time IoT Health Monitoring:")
            for _ in range(3):
                print(iot_monitoring())
                time.sleep(1)

        elif choice == '3':
            print("Exiting. Stay healthy!")
            break

        else:
            print("Invalid choice. Try again.")

# Run the system
main()

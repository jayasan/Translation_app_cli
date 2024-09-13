import os
import openpyxl
from openpyxl import Workbook
from googletrans import Translator, LANGUAGES

# Initialize the Translator
translator = Translator()

# Function to get language code from language name
def get_language_code(language_name):
    language_name = language_name.lower()
    for code, name in LANGUAGES.items():
        if language_name in name.lower():
            return code
    return None

# File paths
excel_file = "translations.xlsx"

# Prompt the user for input
source_text = input("Enter the text to translate: ")
print()  # Adding space
target_language_name = input("Enter the language for translation(e.g., 'Spanish'): ")
print()  # Adding space

# Get the target language code
target_language_code = get_language_code(target_language_name)

if not target_language_code:
    print(f"Error: Language '{target_language_name}' is not supported.")
else:
    try:
        # Detect source language
        detected_language = translator.detect(source_text).lang
        
        # Translate text
        translation = translator.translate(source_text, dest=target_language_code)
        translated_text = translation.text

        print(f"Translated text: {translated_text}")
        print()  # Adding space

        # Save to target.txt
        with open('target.txt', 'w', encoding='utf-8') as file:
            file.write(translated_text)

        # Check if the Excel file exists
        if os.path.exists(excel_file):
            # Load existing workbook
            workbook = openpyxl.load_workbook(excel_file)
            sheet = workbook.active
        else:
            # Create new workbook and sheet
            workbook = Workbook()
            sheet = workbook.active
            sheet.append(["Source Text", "Source Language", "Target Language", "Translated Text"])

        # Append new data
        sheet.append([source_text, LANGUAGES.get(detected_language, 'Unknown'), target_language_name, translated_text])
        workbook.save(excel_file)

        print("Translation saved to target.txt and translations.xlsx.")
        print()  # Adding space

    except Exception as e:
        print(f"Error: {e}")

    # Pause the script
    input("Press Enter to exit...")

Translation Script

Overview

This script translates text from any language to a specified target language using the Google Translate API through the googletrans Python library. It saves both the source and translated text into a target.txt file and appends the data to a translations.xlsx Excel file.

Features

Translate text from any language to a target language.
Save the translated text to target.txt.
Append source text, source language, target language, and translated text to translations.xlsx.

Requirements

Python 3.12.6
Libraries:
 googletrans==4.0.0-rc1 (for Google Translate functionality)
 openpyxl (for handling Excel files)

You can install the required libraries using the following commands:

bash :- pip install googletrans==4.0.0-rc1 openpyxl

Setup

Clone or Download: Clone or download this repository to your local machine.
Install Dependencies: Ensure Python 3.x is installed. Install the necessary Python libraries using pip.

bash :-pip install googletrans==4.0.0-rc1 openpyxl
Prepare Files: Ensure you have the script file (translate_script.py) ready in your working directory.

Usage
Run the Script: Execute the script using Python.

bash:- python translate_script.py

and Follow the Prompts.

License
This project is licensed under the MIT License. See the LICENSE file for details.

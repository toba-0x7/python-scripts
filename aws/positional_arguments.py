# From: https://catalog.us-east-1.prod.workshops.aws/workshops/3d705026-9edc-40e8-b353-bdabb116c89c/en-US/arguments/lab-4/step-1
# Positional arguments - order that the argument is passed to the function depends on order within [ ]

import boto3

def translate_text(text, source_language_code, target_language_code): #Define positional arguments here
    client = boto3.client('translate')
    response = client.translate_text(
        Text=text, # Remove hard coded value and reference 1st argument
        SourceLanguageCode=source_language_code, # Reference 2nd argument
        TargetLanguageCode=target_language_code # Reference 3rd argument
    )
    print(response) 

def main():
    translate_text('I am learning to code in AWS', 'en', 'fr')

if __name__=="__main__":
    main()


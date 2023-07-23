# From: https://catalog.us-east-1.prod.workshops.aws/workshops/3d705026-9edc-40e8-b353-bdabb116c89c/en-US/arguments/lab-4/step-2
# Keyword argument is a name-value pair that is passed to a function
# When using ** we can pass an abritrary number of keyword arguments and reduce the lines of code

import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

def main():
    translate_text(Text='I am learning to code in AWS',SourceLanguageCode='en', TargetLanguageCode='fr')

if __name__=="__main__":
    main()

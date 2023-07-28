# Documentation: https://catalog.us-east-1.prod.workshops.aws/workshops/3d705026-9edc-40e8-b353-bdabb116c89c/en-US/inputs/lab-5/step-4

# PYTHON CONVERSION --> TO JSON
# dict --> object
# list, tuple --> array
# str --> string
# int, float --> number
# True --> true
# False --> false
# None --> null

# JSON package is standard Python package so no need to install
# json.load() and json.dump --> Use to input and output JSON from files and into files
# json.loads() and json.dumps --> Use to input and outputting JSON from strings and into strings (s)

import json

# This uses a json string as an input 

json_string = """
{
    "Input":[
        {
        "Text":"I am learning to code in AWS",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr",
        "Required": true
        }
    ]
}
"""

def main():
    json_input = json.loads(json_string) # Loads the string and converts to JSON
    indented_format = json.dumps(json_input, indent=2) # Converts string back to valid Python data types # indent=2 makes it easier to read
    print(indented_format)

if __name__=="__main__":
    main()


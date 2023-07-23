# Define Imports
import argparse
import json
import boto3

# Arguments; use argparse to give CLI inputs; argument is --file
parser = argparse.ArgumentParser(description="Provides translation  between one source language and another of the same set of languages.")
parser.add_argument(
    '--file',
    dest='filename',
    help="The path to the input file. The file should be valid json",
    required=True)

args = parser.parse_args()

# Functions
# This function opens the file using "with open" and makes it into a Python object called "file_object"
def open_input():
    with open(args.filename) as file_object:
        contents = json.load(file_object)
        return contents['Input'][0]

# This function is standard American Translate function which accepts an arbitray number of keyword arguments
def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

# Main Function - use to call other functions in the order specified
def main():
    kwargs = open_input()
    translate_text(**kwargs)

if __name__ == "__main__":
    main()

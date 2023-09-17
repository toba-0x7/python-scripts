import os
import re

def number_ipynb_files(directory):
    ipynb_files = [file for file in os.listdir(directory) if file.endswith('.ipynb')]

    for idx, ipynb_file in enumerate(ipynb_files, start=1):
        old_path = os.path.join(directory, ipynb_file)
        new_filename = f"{idx:03d}_{ipynb_file}"  # Prefix with a 3-digit number
        new_path = os.path.join(directory, new_filename)
        
        os.rename(old_path, new_path)
        print(f"Renamed: {ipynb_file} -> {new_filename}")

if __name__ == "__main__":
    directory = input("Enter the directory path where IPython Notebook files are located: ")
    number_ipynb_files(directory)

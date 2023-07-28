# HOW TO INPUT DATA FROM A FILE AS AN EXTERNAL SOURCE
# Documentation: https://catalog.us-east-1.prod.workshops.aws/workshops/3d705026-9edc-40e8-b353-bdabb116c89c/en-US/inputs/lab-5/step-3

# To input data from external file, use the format:
# with open(<filename>, 'r') as variable_name: # Insert name of file into filename and delete <>
    # <Do something with the variable here> # Insert command here
    
def open_input(file):
    with open(file, 'r') as f:
        text = f.read() # Use read() to read the actual contents of the file
        print(text)

def main():
    open_input("testfile.txt") # Insert name of file (when tested, this is having a hard time finding the file)

if __name__=="__main__":
    main()

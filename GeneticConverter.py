# Python script to convert data to DNA and reverse
# Developed by: Dallas Hobgood
# Git Hub: https://github.com/wdhobgood/DataToDNAConverter.git
#-------------------------------------------------

# Import
import base64
import tkinter as tk
from tkinter import filedialog

# TKinter setup
root = tk.Tk()
root.withdraw()

# Binary to nucleotide
DNA_encoding = {
    "00": "A",
    "01": "G",
    "10": "C",
    "11": "T"
}

# Nucleotide to binary
BINARY_encoding = {
    "A": "00",
    "G": "01",
    "C": "10",
    "T": "11"
}

# Define more lists
DNAlist = []
BINARYlist = []
BinarySequence = []

# Functions
def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')

def menuState():
    # Ask the user what they want to convert
    var_type = input("What is your input? (text, dna, file) ")
    return(var_type)
def MenuItem(m):
    if m == "text": # If user Input is text
        # Prompt user by asking what text string they would like to convert to a nucleotide sequence.
        text_str = input("What text would you like to convert? ")
        
        # Convert text to binary in "byte" format
        binary_str = ''.join(format(x, '08b') for x in bytearray(text_str, 'utf-8'))

        # Convert byte format to simple 1 and 0 list 2 digits at a time (i.e. 00, 01, 10, 11)
        BINARYlist = [binary_str[i: i+2] for i in range(0, len(binary_str), 2)]

        # Iterate through the 1 and 0 list and where a 2 digit match is found in the dna_encoding list pull the appropriate nucleotide into a new list.
        for num in BINARYlist:
            for key in list(DNA_encoding.keys()):
                if num == key:
                    DNAlist.append(DNA_encoding.get(key)) # The new nucleotide list based on the 2 digit binary combination

        # Move nucleotide sequence from a list to a string value.
        DNA_str = "".join(DNAlist)

        # Print input text, binary code and DNA sequence
        print("The string after binary conversion is :" + "\n" + binary_str + "\n")
        print("DNA sequence is:" + "\n" + DNA_str + "\n")
    elif m == "dna":
        str_data =' ' # Ensure variable is empty

        # Prompt the user by asking what type of file format will the end result be.
        output_type = input("File format are we encoding too? (Ex. string, .gif, .pdf, .mp3) ")

        #Prompt the user to select a text file containing the nucleotide sequence
        file_path = filedialog.askopenfilename()

        # Open the file in read mode
        fileopen = open(file_path, "r")

        # Set variable equal to the contents of the text file.
        text_str = fileopen.read()

        # Gather the nucleotide sequence and set it equal to variable, 1 digit at a time
        BINARYlist = [text_str[i] for i in range(0, len(text_str), 1)]

        # Iterate over the necleotide list and where a match is found, bring back the 2 digit binary code associated.
        for num in BINARYlist:
            for key in list(BINARY_encoding.keys()):
                if num == key:
                    BinarySequence.append(BINARY_encoding.get(key))
        binary_str = "".join(BinarySequence) # The new binary string based on the single digit nucleotide sequence

        #If output type was equal to "string" then decode it differently
        if output_type == "string":
            str_data = decode_binary_string(binary_str)
            # Save the string to a file
        else:
            # Convert binary string to Byte data
            ByteData = bitstring_to_bytes(binary_str)
            
            # Convert Binary to Base64
            Base64format = base64.b64encode(ByteData) # Convert to base64
            with open('Decoded_File' + output_type, 'wb') as decodedfile: # Create a writable file based on user inputed file format
                decodedfile.write(base64.b64decode(Base64format))

        # Ouput message to user
        print ("Decoded_File" + output_type + " was created successfully in the root program directory.")
    elif m == "file":
        # Prompt the user to select a file on their disk that they want to convert to a necleotide sequence
        file_path = filedialog.askopenfilename()
        
        with open(file_path, 'rb') as file: # Open binary file in read binary mode
            # Convert to base64
            encoded_file = base64.b64encode(file.read()) 

            # Convert to bytes
            binaryfile = base64.decodebytes(encoded_file)

            # Format the bytes as binary.
            BinaryString = "".join(["{:08b}".format(x) for x in binaryfile])

        # Group Binary stirng into a 2 digit list (i.e. 00, 01, 10, 11)
        BINARYlist = [BinaryString[i: i+2] for i in range(0, len(BinaryString), 2)]

        # Iterate over the binary list and where a match is found, bring back the associated Nucleotide sequence.
        for num in BINARYlist:
            for key in list(DNA_encoding.keys()):
                if num == key:
                    DNAlist.append(DNA_encoding.get(key))

        # Convert binary list to a binary string. READABLE)
        DNA_str = "".join(DNAlist)

        # Print the binary string
        with open('NucleotideSequence.txt', 'w') as nucleotidefile: # Create a writable file of the nucleotide sequence
                nucleotidefile.write(DNA_str)

        #Output to user this nucleotide sequence file was created.
        print ("NucleotideSequence.txt created successfully in the root program directory.")

# Begin Loop
while True:

    # Main menu
    var_type = menuState()
    MenuItem(var_type)

    

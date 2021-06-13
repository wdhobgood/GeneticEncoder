# Python script to convert data to DNA and reverse
# Developed by: Dallas Hobgood
# Git Hub: https://github.com/wdhobgood/DataToDNAConverter.git
#-------------------------------------------------

# Import
from tkinter.constants import TRUE
from HammingCode import emitterConverter, receptorConverter
import datetime
import base64
from optparse import OptionParser
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
NucleotideList = []
BinarySequence = []
fourBitBinarySequence = []
bitsWithParity = []
bytedata = []

# Functions

def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')

def ConvertToFourBits(s):
    fourBitBinarySequence = [s[i: i+4] for i in range(0, len(s), 4)]
    return(fourBitBinarySequence)

def Main():
    # Set Parser Options
    parser = OptionParser('usage %prog '+\
        '-p (Parity) -f (File) -d (DNA) -D (Debug)')
    parser.add_option("-p", "--parity", action="store_true", dest="parity",
                    help="Initializes Parity (Hamming Code 7:4)")
    parser.add_option("-f", "--file", action="store_true", dest="file",
                    help="Select a file to convert to a nucleotide sequence")
    parser.add_option("-d", "--dna", action="store_true", dest="dna",
                    help="Select a DNA sequence file .txt")
    parser.add_option("-D", "--debug", action="store_true", dest="Debug",
                    help="Ouput debug files")

    (options, args) = parser.parse_args()
    
    if options.file:
        
        # Prompt the user to select a file on their disk that they want to convert to a necleotide sequence
        file_path = filedialog.askopenfilename()
        
        with open(file_path, 'rb') as file: # Open binary file in read binary mode
            # Convert to base64
            encoded_file = base64.b64encode(file.read()) 

            # Convert to bytes
            binaryfile = base64.decodebytes(encoded_file)

            # Format the bytes as binary.
            BinaryString = "".join(["{:08b}".format(x) for x in binaryfile])
        
        #Group binary string into a 4 digit list
        bit_data = ConvertToFourBits(BinaryString)
        
        if options.Debug:
            with open('BinarySequenceWithOutParity.txt', 'w') as binaryFile:
                binaryFile.write(str(BinaryString))

        #Create parity bits if applicable
        if options.parity:
            bitsWithParity = emitterConverter(4, BinaryString)

            bits = "".join(bitsWithParity)
        else:
            bits = BinaryString

        if options.Debug:
            with open('BinarySequenceWithParity.txt', 'w') as binaryFile:
                binaryFile.write(str(bits))

        # Group Binary string into a 2 digit list (i.e. 00, 01, 10, 11)
        BINARYlist = [bits[i: i+2] for i in range(0, len(bits), 2)]

        if options.Debug:
            with open('test.txt', 'w') as binaryFile:
                binaryFile.write(str(BINARYlist))

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

    if options.dna:
        
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
        NucleotideList = [text_str[i] for i in range(0, len(text_str), 1)]
        if options.Debug:
            with open('NucleotideList.txt', 'w') as binaryFile:
                binaryFile.write(str(NucleotideList))

        # Iterate over the necleotide list and where a match is found, bring back the 2 digit binary code associated.
        for num in NucleotideList:
            for key in list(BINARY_encoding.keys()):
                if num == key:
                    BinarySequence.append(BINARY_encoding.get(key))
        binary_str = "".join(BinarySequence) # The new binary string based on the single digit nucleotide sequence
        if options.Debug:
            with open('returnedBinaryString.txt', 'w') as binaryFile:
                binaryFile.write(str(binary_str))

        # Remove Parity Bits if applicable
        if options.parity:
            finalSequence, ack = receptorConverter(4, binary_str)
        else:
            finalSequence = binary_str
            ack = TRUE
        now = datetime.datetime.now()
        if ack:
            with open('Log.txt', 'w') as binaryFile:
                binaryFile.write(str(now) + " | No Issues Found")
        else:
            with open('Log.txt', 'w') as binaryFile:
                binaryFile.write(str(now) + " | Issues Found")

        if options.Debug:
            with open('returnedBinaryWithoutParity.txt', 'w') as binaryFile:
                binaryFile.write(str(finalSequence))
        
        #Convert list to string
        strProcessedBinary = ''.join(finalSequence)
        ByteData = bitstring_to_bytes(strProcessedBinary)
        # Convert Binary to Base64
        Base64format = base64.b64encode(ByteData) # Convert to base64
        with open('Decoded_File' + output_type, 'wb') as decodedfile: # Create a writable file based on user inputed file format
            decodedfile.write(base64.b64decode(Base64format))

        # Ouput message to user
        print ("Decoded_File" + output_type + " was created successfully in the root program directory.")

    
if __name__ == '__main__':
    Main()
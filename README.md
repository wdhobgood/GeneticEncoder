# Genetic Converter / DataToDNAConverter

Encoding a file to nucleotide sequence
--------------------------------------
1. Run from the command line (i.e. python %prog <options>)
2. Options:
  -h, --help    show this help message and exit
  -p, --parity  Initializes Parity (Hamming Code 7:4)
  -f, --file    Select a file to convert to a nucleotide sequence
  -d, --dna     Select a DNA sequence file .txt
  -D, --debug   Ouput debug files
  
3. When type -f or --file, a prompt will appear to select the file you want to encode to a nucleotide sequence. I have tested the following file formats: 
  (.txt / .pdf / .wav / .xlsx / .gif /.jpg / .pptx)
  
  I assume it should work for any file format.
  
  After selecting the file, the program will convert the file to binary and then from binary to a nucleotide sequence based on a simple mapping.
  
 4. Once the program has ran succesfully a new file will be created called, "NucleotideSequence.txt" that will reside in the root directory of the program.
  
    This nucleotide sequence then can be further used in downstream applications.
  
Decoding a nucleotide sequence back to original file format
------------------------------------------------------------
1. Run from the command line (i.e. python %prog <options>)
2. type -d or --dna.
3. Next enter the file extension you are expecting. (ex: .pdf, .jpg, .wav) *Important: You must include the "." before the file extension.*
4. Next a prompt will appear to select a nucleotide sequence (format .txt)

After selecting the text file, the program will read the nucleotide sequence from the .txt file decode the sequence to binary based on a simple mapping and format the binary to byte type data and save it with the file extension you specified above to the root directory of the program titled, "Decoded_File.<your extension>"
  
NOTE: You may choose to review the Log.txt file. If a parity descrepancy exists, Issues will be found.
  
Special options:
 -p | You may include to encode and decode the nucleotide sequence with Hamming Code (7:4) parity bits. in both options when you are encoding and decoding you must use the -p option. (ex. python DNAConverter.py -f -p || python DNAConverter.py -d -p)
  
 -D | you may choose to output files for debugging. this will create numerous files to the root directory for each step of the program.
 

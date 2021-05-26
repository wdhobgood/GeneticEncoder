# Genetic Converter / DataToDNAConverter

Encoding a file to nucleotide sequence
--------------------------------------
1. Run 'python GeneticConverter.py'
2. Start by typing 'file', hit enter
3. A prompt will appear to select a file you want to encode to a nucleotide sequence. I have tested the following file formats: 
  (.txt / .pdf / .wav / .xlsx / .gif /.jpg / .pptx)
  
  I assume it should work for any file format.
  
  After selecting the file, the program will convert the file to binary and then from binary to a nucleotide sequence based on a simple mapping.
  
 4. Once the program has ran succesfully a new file will be created called, "NucleotideSequence.txt" that will reside in the root directory of the program.
  
  This nucleotide sequence then can be further used in downstream applications.
  
Decoding a nucleotide sequence back to original file format
------------------------------------------------------------
1. Run 'python GeneticConverter.py'
2. Start by typing 'dna', hit enter
3. Next enter the file extension you are expecting. (ex: .pdf, .jpg, .wav) *Important: You must include the "." before the file extension.*
4. A prompt will appear to select a text file. as a simple test, you can select the NucleotideSequence.txt you crated in the above.

  After selecting the file, the program will read the nucleotide sequence from the .txt file decode the sequence to binary based on a simple mapping and format the binary to byte type data and save it with the file extension you specified above to the root directory of the program titled, "Decoded_File.<your extension>"
  
 Thats it!
 
  NOTE: Functionality for the "text" option is untested, but likely to follow the same rules. But you may want to consider putting the text in a .txt file and running it that way.

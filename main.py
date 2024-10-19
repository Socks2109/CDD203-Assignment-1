"""
This file prints the transcribed and reverse transcribed DNA
in the terminal.
"""


from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    TODO: The main function
    """
    # Create instance of FastaParser
    aparser = FastaParser('data/test.fa')
    # Create instance of FastqParser
    qparser = FastqParser('data/test.fq')
    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
    print("Transcribe FastAParser:" + "\n")
    for tup in aparser:
        print(transcribe(tup[1]))
    print()

    # For each record of FastqParser, Transcribe the sequence
    # and print it to console
    print("Transcribe FastQParser:" + "\n")
    for tup in qparser:
        print(transcribe(tup[1]))
    print()

    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
    print("Reverse Transcribe FastAParser:" + "\n")
    for tup in aparser:
        print(reverse_transcribe(tup[1]))
    print()
    
    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console
    print("Reverse Transcribe FastQParser:" + "\n")
    for tup in qparser:
        print(reverse_transcribe(tup[1]))

"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()

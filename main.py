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
    typeTranscribeFastA(aparser, transcribe)

    # For each record of FastqParser, Transcribe the sequence
    # and print it to console
    typeTranscribeFastQ(qparser, transcribe)

    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
    typeTranscribeFastA(aparser, reverse_transcribe)
    
    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console
    typeTranscribeFastQ(qparser, reverse_transcribe)

def typeTranscribeFastA(aparser, transcription):
    with open('data/test.fa') as f:
        header = ""
        sequence = ""
        for line in f:
            line = line.strip()
            if line[0] == ">":
                header = line
            else:
                sequence = line
                print(aparser._get_record(header + "," + transcription(sequence)))
    print()

def typeTranscribeFastQ(qparser, transcription):
    with open('data/test.fq') as f:
        header = ""
        sequence = ""
        quality = ""
        checkPlus = False
        for line in f:
            line = line.strip()
            if line[0] == "@":
                header = line
            elif line[0] == "+":
                checkPlus = True
                continue
            elif checkPlus == True:
                quality = line
                print(qparser._get_record(header + "\t" + transcription(sequence) + "\t" + quality))
                checkPlus = False
            else:
                sequence = line
    print()

"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()

"""
Transcribes or reverse transcribes DNA to RNA
"""


def transcribe(seq: str) -> str:
    """
    Transcribes DNA to RNA by converting A -> U, C -> G,
    T -> A, G -> C.
    """
    result = ""
    for i in seq:
        if (i == "A"):
            result += "U"
        elif (i == "C"):
            result += "G"
        elif (i == "T"):
            result += "A"
        elif (i == "G"):
            result += "C"
        else:
            raise Exception("Please check the file for invalid genomic string")
    return result

def reverse_transcribe(seq: str) -> str:
    """
    Transcribes DNA to RNA by converting A -> U, C -> G,
    T -> A, G -> C, then reverses the RNA.
    """
    result = transcribe(seq)
    return result[::-1]

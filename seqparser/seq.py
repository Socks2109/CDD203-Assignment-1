# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    TODO: transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement
    """
    result = ""
    for i in seq:
        if (i == "A"):
            result += "U"
        elif (i == "C"):
            result += "G"
        elif (i == "T"):
            result += "A"
        else:
            result += "C"
    return result

def reverse_transcribe(seq: str) -> str:
    """
    TODO: transcribes DNA to RNA then reverses
    the strand
    """
    result = transcribe(seq)
    return result[::-1]

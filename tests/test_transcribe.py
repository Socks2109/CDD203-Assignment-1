"""
This file tests the trascribe and reverse_transcribe classes.
"""

import pytest
from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Tests the transcribed sequences and makes sure it matches the result.
    Also checks for invalid strings in the file, and makes sure an error is raised
    """
    seq = ["ACTGAACCC", "AAAAAA"]
    result = ["UGACUUGGG", "UUUUUU"]
    for i, gene in enumerate(seq):
        assert transcribe(gene) == result[i]
    with pytest.raises(Exception, match="Please check the file for invalid genomic string"):
        transcribe("AHACTGCCC")

def test_reverse_transcribe():
    """
    Tests the reverse transcribed sequences and makes sure it matches the result.
    Also checks for invalid strings in the file, and makes sure an error is raised.
    """
    seq = ["ACTGAACCC", "TCGAGTG"]
    result = ["GGGUUCAGU", "CACUCGA"]
    for i, gene in enumerate(seq):
        assert reverse_transcribe(gene) == result[i]
    with pytest.raises(Exception, match="Please check the file for invalid genomic string"):
        transcribe("AHACTGCCC")

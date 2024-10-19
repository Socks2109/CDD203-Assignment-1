"""
This file tests the FastaParser and FastqParser classes.
"""

from seqparser import (
        FastaParser,
        FastqParser)


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    This function asserts that the first two lines in the example Fasta file can be read and be placed in
    a tuple with the form (header, sequence)
    """
    aparser_test = FastaParser("data/test.fa")
    result = [(">seq0", "TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA"), 
              (">seq1", "TCCGCCCGCTGTGCTGACGAGACTAGCAGGGAAATAAATAGAGGGTTTAGTTATACTCAGTAGGCAGTTCGATGGCTTATATCTAACTTCTTATTCCGAT")]
    for i, line in enumerate(aparser_test):
        if i <= 1:
            assert line == result[i]


def test_FastqParser():
    """
    This function asserts that the first two lines in the example Fastq file can be read and be placed in
    a tuple with the form (header, sequence, quality)
    """
    qparser_test = FastqParser("data/test.fq")
    result = [("@seq0", "TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG", "*540($=*,=.062565,2>\'487\')!:&&6=,6,*7>:&132&83*8(58&59>\'8!;28<94,0*;*.94**:9+7\"94(>7=\'(!5\"2/!%\"4#32="),
              ("@seq1", "CCCCGGACGACTGATCCCGATAGAGCTCACTCTTCGAGGCAAGCAGACCCATATCGTCCTGCTGGCAACGCTATCCGGGTGCGAGTAAATCGAAACCTCG", "\'(<#/0$5&!$+,:=%7=50--1;\'(-7;0>=$(05*9,,:%0!<),%646<8#%\".\"-\'*-0:.+*&$5!\'8)(%3*+9/&/%=363*,6$20($97,\"")]
    for i, line in enumerate(qparser_test):
        if i <= 1:
            assert line == result[i]

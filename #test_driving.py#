
"""
Making an LLS integrator
Inputs:
 1) All possible nodes
  a. uses -n flag followed by file name
  b. nodes have alphanumeric names
  c. there is no node with no name (!="")
  d. the file is not empty
  e. the nodes are separated by commas
 2) Gold standard(s)
  a. uses -g flag followed by file name
  b. the file is not empty
  c. nodes match the nodes from all possible nodes
  d. edges are node1;node2,weight12;node3,weight13 format
  e. different initial nodes are on different lines
 3) Experimental data
  a. uses the -e flag followed by file name
  b. the file is not empty
  c. nodes match the ndoes from all possible nodes
  d. edges are node1;node2,weight12;node3,weight13 format
  e. different initial nodes are on different lines
 4) Output name
  a. uses the -o flag followed by a file name
 5) Optional weighting paramter
  a. uses the -w flag followed by a number
  b. number is not zero
  c. number is not negative


Calculation:
 1)LLS
  a) Does not return zero in denominator of LLS equation
  b) Does not return zero in denominator of bottom of LLS equation
  c) Does not return zero in denominator of top of LLS equation
  d) Does not return NaN
 2) WS
  a) Does not have zero in the denominator
  b) Does not have a negative number in the denominator
  c) Does not give a negative number as output 

"""
import unittest

class BadInputNodes(unittest.TestCase):
    def BadFlag(self):
        "input should use -n flag followed by file name"
        pass
    def AlphaNum(self):
        "nodes should have alphanumeric names"
        pass
    def NoBlankNodes(self):
        "nodes should not have a "" name"
        pass
    def EmptyFile(self):
        "the file called should not be empty"
        pass
    def CommaNodes(self):
        "the nodes should be in list separated by commas"
        pass

class BadGoldStandard(unittest.TestCase):
    def BadFlag(self):
        "input should use -g flag followed by file name"
        pass   
    def EmptyFile(self):
        "the file called should not be empty"
        pass
    def NodeMatch(self):
        "the nodes should match the nodes in the all-nodes file"
        pass
    def EdgeFormat(self):
        "edges are node1;node2,weight12;node3,weight13 format"
        pass
    def EdgesSeparated(self):
        "different initial nodes are on different lines"
        pass
    
class BadExpData(unittest.TestCase):
    def BadFlag(self):
        "input should use -e flag followed by file name"
        pass   
    def EmptyFile(self):
        "the file called should not be empty"
        pass
    def NodeMatch(self):
        "the nodes should match the nodes in the all-nodes file"
        pass
    def EdgeFormat(self):
        "edges are node1;node2,weight12;node3,weight13 format"
        pass
    def EdgesSeparated(self):
        "different initial nodes are on different lines"
        pass

class BadOutput(unittest.TestCase):
    def BadFlag(self):
        "input should use -o flag follwed by file name"
        pass

class BadParameter(unittest.TestCase):
    def BadFlag(self):
        "input should use -w flag follwed by number"
        pass
    def NotZero(self):
        "input number should not be zero"
        pass
    def NotNeg(self):
        "input number should not be negative"
        pass












A:1
B:2
C:3



1, (2, 0.5, 0), (3, 0.3, 1). (4, 1, 1)
2, (1, 0.5, 0)
3, (1, 0.3, 1)
4, (1, 1, 2)


1, (2, 0.5), (3, 0.3), (4, 1)
2, (1, 0.5)
3, (1, 0.3)
4, (1, 1)



Node A, (Node B, .5), (Node C, .3)
Node B, (Node A, .5), (Node D, blach)



"""
Three core processes
0) Compare a graph to a gold standard
1) LLS gives LLS's to graphs
2) WS puts it all together

a) Input
 -hard to test, maybe not necessary
b) Parsing
c) Calculating
d) Writing

"""

Parse_tsv.py
============

#!/usr/bin/env python

import re

class HeaderParser():
    """Useful for making sense of a header line."""
    def extract_zt(self, s):
        """From a column label, gets numerical ZT time."""
        assert "ZT" in s
        m = re.search("ZT([0-9]\.?[0-9]*)", s)
        if m == None:
            raise Exception("Badly formed ZT time, bro!")
        return float(m.group(1))
    def parse_header(self, h, f=None):
        """Gets a list of ZT times from a header."""
        if f == None:
            f = self.extract_zt
        return [f(w) for w in h.split()[1:]]


Parsetsv_spec.py
================
#!/usr/bin/env python

import unittest
import random
from parsetsv import HeaderParser

class ExtractZTSpec(unittest.TestCase):
    """Describe the method for pulling a ZT time out of a column label."""
    def setUp(self):
        self.parser = HeaderParser()
    def test_zt_requirement(self):
        """It should require that a ZT substring be in the label."""
        test_passes = False
        try:
            self.parser.extract_zt("FOOBAR")
            test_passes = False
        except:
            test_passes = True
        self.assertTrue(test_passes)
    def test_time_requirement(self):
        """It should require that some form of time be in the label."""
        test_string = "AlanTimeZT"
        test_passes = False
        try:
            self.parser.extract_zt(test_string)
            test_passes = False
        except:
            test_passes = True
        self.assertTrue(test_passes)
    def test_integral_time(self):
        """It should handle integral times correctly."""
        test_time   = random.randint(0,24)
        test_string = "AlanTimeZT{0}".format(test_time)
        self.assertEquals(self.parser.extract_zt(test_string), test_time)
    def test_decimal_time(self):
        """It should handle floating point times correctly."""
        test_time   = random.random() * 24
        test_string = "AndyTimeZT{0}".format(test_time)
        expected = test_time
        computed = self.parser.extract_zt(test_string)
        delta = computed - expected
        self.assertTrue(delta < 0.001)
    def test_nonsense_decimal(self):
        """ . by itself should not be a time."""
        test_passes = False
        try:
            self.parser.extract_zt("ZT.")
            test_passes = False
        except Exception as e:
            test_passes = True
        self.assertTrue(test_passes)

class ParseHeaderSpec(unittest.TestCase):
    """Describe the method for parsing a WHOOOOOLE header line!"""
    def setUp(self):
        self.parser = HeaderParser()
    def test_empty_case(self):
        """It should return empty list for no ZT's."""
        self.assertEquals([], self.parser.parse_header("", extract_mock))
        self.assertEquals([], self.parser.parse_header("#\t", extract_mock))
    def test_discard_first(self):
        """It should lose the first item in the list."""
        test_length = random.randint(0,100)
        test_string = "#\t{0}".format("\t".join(map(str, xrange(test_length))))
        expected = test_length
        computed = len(self.parser.parse_header(test_string, extract_mock))
        self.assertEquals(expected, computed)
    def test_correct_parsing(self):
        """It should [somewhat trivially] do the right thing."""
        test_length = random.randint(0,100)
        test_string = "#\t{0}".format("\t".join(map(str, xrange(test_length))))
        expected = [extract_mock(s) for s in xrange(test_length)]
        computed = self.parser.parse_header(test_string, extract_mock)
        self.assertEquals(expected, computed)
    def test_default_parser(self):
        """It should choose a sensible default -- ZT parsing."""
        stringit = lambda s: "ZT{0}".format(s)
        test_length = random.randint(0,100)
        test_string = "#\t{0}".format("\t".join(map(stringit, xrange(test_length))))
        expected =  range(test_length)
        computed = self.parser.parse_header(test_string)
        self.assertEquals(expected, computed)

class AcceptanceSpec(unittest.TestCase):
    """Define integrated behaviour."""
    def test_mock_parsing(self):
        """It should correctly parse that fake header in header.mock."""
        parser = HeaderParser()
        self.assertEquals(
            parser.parse_header(open("header.mock",'r').readline()),
            [2,4,6,8,10,12]
        )

def extract_mock(s):
    return "!{0}+@".format(s)

if __name__ == "__main__":
    unittest.main()


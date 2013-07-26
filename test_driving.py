
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

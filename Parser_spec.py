#!/usr/bin/env python

from Parser import NodeParser
import unittest

class ExtractNodes(unittest.TestCase):
    """Make sure nodes are pulled out correctly"""
    def setUp(self):
        self.parser = NodeParser()
    def test_commas(self):
        """Make sure that commas are in the file"""
        test_passes = False
        try: 
            self.parser.extract_nodes("no_commas")
            test_passes = False
        except Exception as e:
            print(e)
            test_passes = True
        self.assertTrue(test_passes)
    def test_no_empty(self):
        """Make sure there are no empty nodes"""
        test_passes = False
        try:
            self.parser.extract_nodes("all_commas")
            test_passes = False
        except:
            test_passes = True
        self.assertTrue(test_passes)
    def test_find_node(self):
        """Make sure there are only alphanumeric nodes in file"""
        test_passes = False
        try:
            self.parser.extract_nodes("bad_nodes")
            test_passes = False
        except Exception:
            test_passes = True
        self.assertTrue(test_passes)

    def test_assign_no(self):
        """Does assign_no_to_node give dict and list?"""
        test_list = []
        for i in xrange(random.randint(0,100)):
            test_length = random.randint(0,100)
            test_string = "#\t{0}".format("\t".join(map(str, xrange(test_length))))
            test_list.append(test_string)
        self.parser.assign_no_to_node(test_list)
        ##### Still need to write the asserts and errors 

    def test_assign_node_num(self):
        """Give every node a number value in dict"""
        pass

class ExtractEdges(unittest.TestCase)

    def test_read_random_edges(self):
        """Make sure the edges are entered correctly
        Should be in a Node, (Node,#),(Node, #) format)"""
        pass


    def 


class CompareEdges(self):

    



if __name__ == "__main__":
    unittest.main()

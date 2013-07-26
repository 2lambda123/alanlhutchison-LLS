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
            self.parser.extract_nodes("parse_test")
            test_passes = False
        except:
            test_passes = True
        self.assertTrue(test_passes)
    def test_find_node(self):
        """Make sure there are alphanumeric nodes in file"""
        test_passes = False
        try:
            self.parser.extract_nodes("all_commas")
            test_passes = False
        except:
            test_passes = True
        self.assertTrue(test_passes)




if __name__ == "__main__":
    unittest.main()

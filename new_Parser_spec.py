#!/usr/bin/env python


from new_Parser import Graph
from new_Parser import EdgeParser
from new_Parser import Dict2Array
from new_Parser import Array_Parser
from new_Parser import pickle_Array_Parser
from new_Parser import pickle_to_readable
from new_Parser import NodeParser


import unittest
import random
import string


class checkGraph(unittest.TestCase):
    """Make sure graph has all the right attributes"""
    def setUp(self):
        self.graph = Graph()

    def test_nodes_not_empty(self):
        """Make sure the nodes are not empty"""
        empty = []
        test_passes = False
        try:
            d = self.graph.Nodes(empty)
            test_passes = False
        except:
            test_passes = True
        self.assertTrue(test_passes)


    def test_nodes_are_Dict(self):
        """Make sure nodes are a dictionary"""    
        pass

    def test_edges_are_array(self):
        """Make sure the edges are a square array"""
        pass
    
    def test_graph_takes_nodes_dict(self):
        """Make sure the graph takes nodes in dict"""
        pass


    def test_graph_takes_edges_dict(self):
        """Make sure the graph takes edges as array"""
        pass


class CheckParser(unittest.TestCase):
    """This will check the parsers"""
    def test_EdgeParser(self):
        pass
    
    def test_Dict2Array(self):
        pass
    
    def test_Array_Parser(self):
        pass

    def test_pickle_Array_Parser(self):
        pass

    def test_pickle_to_readable(self):
        pass

    def test_NodeParser(self):
        pass

if __name__ == "__main__":
    unittest.main()

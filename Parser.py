#!/usr/bin/env python

class NodeParser():
    """Will read nodes from CSV file"""
    def extract_nodes(self,fn):
        """From fn, get csv nodes"""
        with open(fn,'r') as f:
            assert "," in f
            nodes =f.split(",")
            print(nodes[1])
            nodes = [node for node in nodes if node!=""]
        return nodes





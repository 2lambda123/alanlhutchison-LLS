#!/usr/bin/env python

import re
import sys

def main():
    fn = sys.argv[1]
    a = NodeParser()
    a.extract_nodes(fn)


class NodeParser():
    """Will read nodes from CSV file"""
    def extract_nodes(self,fn):
        """From fn, get csv nodes"""
        with open(fn,'r') as f:
            line = f.readline()
            assert "," in line
            assert re.search("[\W][^,]",line) is None
            nodes = line.split(",")
            nodes = [node for node in nodes if (node!="")]
            print nodes
        assert nodes != []
        return nodes


if __name__=="__main__":
    main()


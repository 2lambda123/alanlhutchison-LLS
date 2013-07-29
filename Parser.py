#!/usr/bin/env python

import re
import sys

def main():
    fn = sys.argv[1]
    #a = NodeParser()
    #a.extract_nodes(fn)
    b = EdgeParser()
    b.extract_edges(fn)
class NodeParser():
    """Will read nodes from CSV file"""
    def extract_nodes(self,fn):
        """From fn, get csv nodes"""
        with open(fn,'r') as f:
            line  = f.readline()
            nodes = string_to_nodes(line)
        return nodes

    def string_to_nodes(self,line):
        assert "," in line
        assert re.search("[\W][^,]",line) is None
        nodes = line.split(",")
        nodes = [node for node in nodes if (node!="")]
        assert nodes != []
        nodes = sorted(nodes)
        return nodes

    def assign_no_to_node(self,list):
        list = sorted(list)
        d = {}
        for i,node in iter(list):
            d[node] = i 
        return d,len(d)
    
    def CompareNodes(self,s,list):
        """Is s found in the list? """
        pass

class EdgeParser():
    """Will read edegs from a CSV file"""
    def extract_edges(self,fn):
        """From fn, get edges"""
        new_edges = {}
        with open (fn,'r') as f:
            for line in f:
                new_edges = EdgeParser.line_to_edges(self,line,new_edges)
        return new_edges

    def line_to_edges(self,line,new_edges):
        try:
            assert "," in line
            assert "(" in line
            assert ")" in line
        except Exception as e:
            print(e)
            pass
        edges = line.split("(")
        lead = edges[0].strip()
        lead = lead.strip(",")
        new_edges.setdefault(lead,[])
        for edge in edges[1:]:
            edge = edge.strip("\n")
            edge = edge.strip(" ")
            edge = edge.strip(",")
            edge = edge.strip("\)")
            edge = edge.split(",")
        new_edges[lead].append(edge)
        return new_edges    

    def CompareEdges(self,edge,list):
        """Does edge exist in list? """
        pass

if __name__=="__main__":
    main()


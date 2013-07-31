#!/usr/bin/env python

import re
import sys
import math

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
            nodes = self.string_to_nodes(line)
        return nodes

    def string_to_nodes(self,line):
        assert "," in line
        nodes = line.split(",")
        # takes out empty nodes
        nodes = [node for node in nodes if (node!="")]
        # will remove duplicates
        new_nodes = []
        for node in nodes:
            if node not in new_nodes:
                new_nodes.append(node)
            else:
                print node, "was a duplicate and was removed!"
        nodes = new_nodes
        assert nodes != []
        nodes = sorted(nodes)
        return nodes

    def assign_no_to_node(self,list):
        """list should be unique"""
        list = sorted(list)
        d = {}
        for i,node in enumerate(list):
            #print i,node
            d[node] = i 
        return d,len(d)
    
    def CompareNodes(self,s,list):
        """Return true if s is in list """
        return s in list


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
        assert "," in line
        assert "(" in line
        assert ")" in line
        edges = line.split("(")
        lead = edges[0].strip()
        lead = lead.strip(",")
        lead = lead.strip()
        new_edges.setdefault(lead,[])
        for edge in edges[1:]:
            edge = edge.strip("\n")
            edge = edge.strip(" ")
            edge = edge.strip(",")
            edge = edge.strip("\)")
            edge = edge.split(",")
            edge = (edge[0],float(edge[1]))
            new_edges[lead].append(edge)
        return new_edges    

            
        
class LLS_Calculator():
    """Will calculate an LLS for data"""
    def CompareEdges(self,edge,dict):
        """Does edge exist in list? """
        """Does not assume symmetric edge lists, though you should probably have them"""
        # Edge is a tuple with two nodes
        # Dict is a dictionary of node-keys and tuple (node,float) values
        if edge[0] in dict.keys():
            if edge[1] in [x[0] for x in dict[edge[0]]]:
                return True
            else:
                return False
        else:
            if edge[1] in dict.keys():
                if edge[0] in [x[0] for x in dict[edge[1]]]:
                    return True
                else:
                    return False
            else:
                return False

    def numerator(data,gold):
        """Finds probabilities of edges in data relative to gold"""
        pass


    def denominator(gold,size):
        """Finds probablilites of gold edges relative to all possible edges"""
        pass


    def LLS(num,denom):
        """Returns the LLS"""
        return math.log(num/denom)
        

if __name__=="__main__":
    main()


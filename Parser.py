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

    def numerator(self,data,gold):
        """Finds probabilities of edges in data relative to gold"""
        gold_size = 0.0
        for lead in gold.keys():
            gold_size += len(gold[lead])
            
        epsilon = 0.0000000001
        match = 0.0
        not_match = 0.0
        exp_size = 0.0
        for lead in data.keys():
            for hit in data[lead]:
                exp_size += 1
                edge = (lead,hit[0])
                if self.CompareEdges(edge,gold):
                    match += 1
                else:
                    not_match += 1
        #print gold_size
        #print match
        #print not_match
        #print exp_size
        if match == 0.0:
            match = epsilon
        elif not_match == 0.0:
            not_match = epsilon

        num1 = match / gold_size 
        num2 = not_match / gold_size
        return num1/num2

    def denominator(self,gold,length):
        """Finds probablilites of gold edges relative to all possible edges"""
        size = length * length

        gold_size = 0.0
        for lead in gold.keys():
            gold_size += len(gold[lead])
        
        den1 = gold_size / size
        den2 = (1-gold_size) / size

        return den1/den2


    def LLS(self,num,denom):
        """Returns the LLS"""
        return math.log(num/denom)
        

if __name__=="__main__":
    main()


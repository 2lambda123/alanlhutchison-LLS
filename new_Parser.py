#!/usr/bin/env python

import re
import sys
import math
import numpy as np

def main():
    pass



class Graph():
    """Graph carries edges and nodes"""
    def __init__(self,d_nodes,a_edges):
        self.nodes = d_nodes
        self.edges = a_edges
    
    def give_nodes(self):
        """"This method will return the nodes, but hopefully will be replaced someday"""
        return self.nodes

    def give_edges(self):
        """This method will return the edges, but hopefully will be omitted once
        the methods for this class are better fleshed out"""
        return self.edges

    def Write(self):
        """Will write the nodes and edges as two pkl files"""
        #nodes = self.Nodes()
        #edges = self.Edges()
        pass


"""
==================================================
"""

def EdgeParser(fn):
    """Parses a file of A,(B,0.4),(C,0.3)"""
    """Outputs a dictionary of edges"""
    new_edges = {}
    with open(fn,'r') as f:
        for line in f:
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
            
            nodes = sorted(new_edges.keys())
            d_nodes = {}
            for i,node in nodes:
                d_nodes[node] = i 

    return d_nodes, new_edges    


def Dict2Array(self,d_nodes,d_edges,fn_out):
    size = len(d_nodes.keys())
    table = np.zeros((size,size))
    
    for i,lead in enumerate(d_edges.keys()):
        others = d_edges[lead]
        others = sorted(others)
        weights = np.array([ table[i][d_nodes(other[1])] for other in others])

    output = fn_out
        
    with open(output,'w') as g:
        g.write("!"+",".join(d_nodes.keys())+"\n")
        for line in table:
            g.write(",".join([str(x) for x in line])+"\n")        

    return d_nodes,table

def Array_Parser(self,fn):
    """Takes in a file with !Node_List and Array of length Node_list by Node_list"""
    """Makes a pkl of d_nodes and tables, returns same"""
    
    output = fn
    d_nodes = {}
    with open(fn,'r') as f:
        for line in f:
            assert "," in line
            if line[0]=="!":
                nodes = line.split(",")
                nodes = [node.strip() for node in nodes]
                for i, node in enumerate(nodes):
                    d_nodes[node] = i
            else:
                weights = float(line.split(","))
                size = len(weights)
                table = np.zeros((size,size))
                for i in size:
                    for j in size:
                        table[i][j] = weights[j]                

    out_array = output+"_array.pkl"
    out_nodes = output+"_nodes.pkl"
    with open(out_array,'w') as g:
        pickle.dump(g,table)
    with open(out_nodes,'w') as g:
        pickle.dump(g,d_nodes)

    return d_nodes,table

def pickle_Array_Parser(self,pkl_array,pkl_nodes):
    """Takes in a file with pkled array and d_nodes"""
    """Returns pkled values"""
    with open(pkl_array,'r') as f:
        table = pickle.load(f)
    
    with open(pkl_nodes,'r') as f:
        nodes = pickle.load(f)
    
    return d_nodes,table


def pickle_to_readable(self,pkl_array,pkl_nodes):
    """Takes in a file with pkled array and d_nodes"""
    """Returns readable files"""
    with open(pkl_array,'r') as f:
        table = pickle.load(f)
    
    with open(pkl_nodes,'r') as f:
        nodes = pickle.load(f)
    
    output = "".join(pkl_array.split("_")[:-1])
        
    with open(output,'w') as g:
        g.write("!"+",".join(d_nodes.keys())+"\n")
        for line in table:
            g.write(",".join([str(x) for x in line])+"\n")

    return d_nodes,table

def NodeParser(fn):
    """Parses a list of nodes, outputs a dictionary"""
    with open(fn,'r') as f:
        for line in f:
            assert "," in line:
            nodes = line.split(",")
    nodes = [node.strip for node in nodes]
    nodes = sorted(nodes)
    d_nodes = {}
    for i,node in enumerate(nodes):
        d_nodes[node] = i

    return d_nodes
            

if __name__ == "__main__":
    main()

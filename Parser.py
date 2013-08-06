#!/usr/bin/env python

import re
import sys
import math

def main():
    fn_nodes = "test/node_list"
    fn_gold = "test/gold_edges"
    fn_exp = "test/exp_data"
    a = NodeParser()
    nodes = a.extract_nodes(fn_nodes)
    d_num_nodes, leng = a.assign_no_to_node(nodes)
    
    b = EdgeParser()
    gold_edges = b.extract_edges(fn_gold)
    num_gold_edges = b.EdgeNode2Num(gold_edges,d_num_nodes)
    
    exp_edges = b.extract_edges(fn_exp)
    num_exp_edges = b.EdgeNode2Num(exp_edges,d_num_nodes)
    
    c = LLS_Calculator()

    num = c.numerator(num_exp_edges,num_gold_edges)
    den = c.denominator(num_gold_edges,leng)
    score = c.LLS(num,den)
    print score
    
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
                print("Mazel Tov!", node, "was a duplicate and was removed!")
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
            
    def EdgeNode2Num(self,edges,d_node_num):
        """This program turns edges into their associated integers"""
        new = {}
        for lead in edges.keys():
            new.setdefault(d_node_num[lead],[])
            for hit in edges[lead]:
                new[d_node_num[lead]].append((d_node_num[hit[0]],hit[1]))
        return new


class LLS_Calculator():
    """Will calculate an LLS for data"""
    """
    num = (exp edges in gold) / (all exp edges - exp edges in gold)
    denom = (gold edges from all) / (all edges - gold edges from all)

    """

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
        print gold_size
        epsilon = 0.0000000001
        match = 0.0
        not_match = 0.0
        exp_size = 0.0
        for lead in data.keys():
            for hit in data[lead]:
                exp_size += 1
                edge = (lead,hit[0])
                if self.CompareEdges(edge,gold):
                    print edge
                    match += 1
                else:
                    not_match += 1

        if match == 0.0:
            match = epsilon
        elif not_match == 0.0:
            not_match = epsilon
        print match
        print not_match
        num1 = match 
        num2 = not_match
        return num1/num2

    def denominator(self,gold,length):
        """Finds probablilites of gold edges relative to all possible edges"""
        size = length * (length - 1) 

        gold_size = 0.0
        for lead in gold.keys():
            gold_size += len(gold[lead])
        
        #print 'Whazzup'
        #print gold_size
        #print size
        den1 = gold_size
        den2 = size - gold_size 
        #print den1
        #print den2
        return den1/den2


    def LLS(self,num,denom):
        """Returns the LLS"""
        #print num
        #print denom
        return math.log(num/denom)
        

if __name__=="__main__":
    main()


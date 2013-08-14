#!/usr/bin/env python

import sys
from math import log
import numpy as np
from numpy import matrix 
import scipy
from scipy import sparse
import random
import string as st
from operator import itemgetter
import pickle
import time

def main():
    fn_dict = sys.argv[1]
    fn_gold = sys.argv[2]
    fn_exp = sys.argv[3:]

    input_Staph_spear(fn_dict,fn_gold,fn_exp)
    #input2(fn_dict,fn_gold,fn_exp)


def input_Staph_spear(fn_dict,fn_gold,fn_exp):
    d_nodes = NodeParser(fn_dict)    

    d_gold_edges = SimpleEdgeParser(fn_gold)
    m_gold = Dict2Matrix(d_nodes,d_gold_edges,fn_gold+".Graph")
    g_gold = Graph(d_nodes,m_gold)

    gs_exp = []
    """Next will be to make these different parsing choices flags"""
    for fn in fn_exp:
        d_exp_edges = ThreePartEdgeParser(fn)
        m_exp = Dict2Matrix(d_nodes,d_exp_edges,fn+".Graph")
        print 'Starting Graph ',time.time()
        g_exp = Graph(d_nodes,m_exp)
        print 'Finishing Graph', time.time()
        gs_exp.append(g_exp)

    WeightedSum(gs_exp,g_gold)


def input2(fn_dict,fn_gold,fn_exp):
    d_nodes = NodeParser(fn_dict)    
    d_gold_edges =SimpleEdgeParser(fn_gold)
    m_gold = Dict2Matrix(d_nodes,d_gold_edges,fn_gold+".Graph")
    
    g_gold = Graph(d_nodes,m_gold)

    gs_exp = []
    """Next will be to make these different parsing choices flags"""
    for fn in fn_exp:
        d_exp_edges = SimpleEdgeParser(fn)
        m_exp = Dict2Matrix(d_nodes,d_exp_edges,fn+".Graph")
        g_exp = Graph(d_nodes,m_exp)
        gs_exp.append(g_exp)

    WeightedSum(gs_exp,g_gold)


def test_with_random_data():
    size = random.randint(3,12)
    d = dict(zip([i for i in st.uppercase[:size]],range(size)))
    gold = Graph(d,np.matrix([1 if random.random()>0.7 else 0 for  _ in xrange(size*size)]).reshape((size,size)))
    mat_list = [np.matrix([random.random() \
               for _ in xrange(size*size)]).reshape((size,size)) \
               for __ in xrange(4)]
    graph_list = [Graph(d,mat) for mat in mat_list]
    ws = WeightedSum(graph_list,gold)



class Graph():
    """Graph carries edges and nodes"""
    def __init__(self,d_nodes,mat_edges):
        self.nodes = d_nodes
        self.edges = mat_edges
    
    def give_nodes(self):
        """"This method will return the nodes, but hopefully will be replaced someday"""
        return self.nodes

    def give_edges(self):
        """This method will use a paring function to return a binary sparse array
        of the called edges"""
        print "In give_edges, Generalissimo: ",time.time()
        size = len(self.edges)
        bin = scipy.sparse.lil_matrix(np.zeros((size,size)))
        #bin = np.matrix(np.zeros((size,size)),'bool')
        for (i,j),k in np.ndenumerate(self.edges):
            bin[i,j]=self.thresh((i,j),k)
        print "Filled matrix via thresh, Captain: ",time.time()
        bin = scipy.sparse.csc_matrix(bin)
        print "Made it a CSC, Admiral: ", time.time()
        return bin


    def map_thresh(self,indecies):
        pass
    
    def thresh(self,indecies,weight,var=""):
        """This function will determine how to threshold a given edge """
        #np.ndenumerate gives "(index1,index2), value"
        cutoff = 0.9
        if abs(weight)> 0.9:
            return 1
        else:
            return 0

    def Write(self):
        """Will write the nodes and edges as two pkl files"""
        #nodes = self.Nodes()
        #edges = self.Edges()
        pass


"""
==================================================
"""

def SimpleEdgeParser(fn):
    """Parses a file of A,B \n A,C"""
    """Outputs a dictionary of A:(B,1)"""
    print 'In SimpleEdgeParser ',time.time()
    new_edges = {}
    with open(fn,'r') as f:
        for line in f:
            edges = line.split()
            new_edges.setdefault(edges[0],[])
            new_edges[edges[0]].append((edges[1],1))
            new_edges.setdefault(edges[1],[])
            new_edges[edges[1]].append((edges[0],1))
                 
    return new_edges    

def ThreePartEdgeParser(fn):
    """Parses a file of A \t B \t Weight """
    print 'In ThreePartEdgeParser'
    new_edges = {}
    with open(fn,'r') as f:
        for line in f:
            edges = line.split()
            new_edges.setdefault(edges[0],[])
            new_edges[edges[0]].append([edges[1],edges[2]])
            new_edges.setdefault(edges[1],[])
            new_edges[edges[1]].append([edges[0],edges[2]])

    return new_edges


def EdgeParser(fn):
    """Parses a file of A,(B,0.4),(C,0.3)"""
    """Outputs a dictionary of edges"""
    print 'In EdgeParser ',time.time()
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


def Dict2Matrix(d_nodes,d_edges,fn_out):
    print 'In Dict2Matrix ', time.time()
    size = len(d_nodes.keys())
    mat = np.matrix(np.zeros((size,size)))

    with open(fn_out+".badnodes",'w') as gg:
        for i,lead in enumerate(sorted(d_edges.keys())):
            others = d_edges[lead]
            for other in others:
                if other[0] in d_nodes.keys():
                    mat[i,d_nodes[other[0]]] = other[1]
                else:
                    gg.write(other[0]+"\n")

    output = fn_out
    
    with open(output,'w') as g:
        g.write("!"+",".join(d_nodes.keys())+"\n")
        for line in mat.tolist():
            g.write(",".join([str(x) for x in line])+"\n")        
    return mat

def Matrix_Parser(fn):
    """Takes in a file with !Node_List and Array of length Node_list by Node_list"""
    """Makes a pkl of d_nodes and mat, returns same"""
    print 'In Matrix_Parser ',time.time()
    output = fn
    d_nodes = {}
    with open(fn,'r') as f:
        count = 0 
        for line in f:
            assert "," in line
            if line[0]=="!":
                nodes = line.split(",")
                nodes = [node.strip() for node in nodes]
                for i, node in enumerate(nodes):
                    d_nodes[node] = i
            else:
                weights = [float(x) for x in line.split(",")]
                size = len(weights)
                mat = np.matrix(np.zeros((size,size)))
                for j in size:
                    mat[count,j] = weights[j]                
                count += 1
    out_array = output+"_matrix.pkl"
    out_nodes = output+"_nodes.pkl"
    with open(out_array,'w') as g:
        pickle.dump(g,mat)
    with open(out_nodes,'w') as g:
        pickle.dump(g,d_nodes)

    return d_nodes,mat

def pickle_Matrix_Parser(pkl_matrix,pkl_nodes):
    """Takes in a file with pkled array and d_nodes"""
    """Returns pkled values"""
    print 'In pickle_Matrix_Parser'
    with open(pkl_matrix,'r') as f:
        mat  = pickle.load(f)
    
    with open(pkl_nodes,'r') as f:
        nodes = pickle.load(f)
    
    return d_nodes,mat


def pickle_to_readable(pkl_matrix,pkl_nodes):
    """Takes in a file with pkled array and d_nodes"""
    """Returns readable files"""
    print 'In pickle_to_readable'
    with open(pkl_matrix,'r') as f:
        mat = pickle.load(f)
    
    with open(pkl_nodes,'r') as f:
        nodes = pickle.load(f)
    
    output = "".join(pkl_matrix.split("_")[:-1])
        
    with open(output,'w') as g:
        g.write("!"+",".join(d_nodes.keys())+"\n")
        for line in mat.tolist():
            g.write(",".join([str(x) for x in line])+"\n")

    return d_nodes,mat

def NodeParser(fn):
    """Parses a list of nodes, outputs a dictionary"""
    print 'In NodeParser ', time.time()
    with open(fn,'r') as f:
        for line in f:
            assert "," in line
            nodes = line.split(",")
    nodes = [node.strip() for node in nodes]
    nodes = sorted(nodes)
    d_nodes = {}
    for i,node in enumerate(nodes):
        d_nodes[node] = i

    return d_nodes
            

def sparse_decider(mat):
    """Turns array into matrix, decides if it needs to be sparse or not"""
    print 'In sparse_decider'
    # WRITE SOME KIND OF DECIDER TO MAKE IT SPARSE OR NOT
    return mat

"""
==============================
"""
def CompareGraphs(exp,gold_bin):
    """Take a Graph object and compare it to another"""
    print 'In CompareGraph ', time.time()
    exp_bin = exp.give_edges()
    print "Methinks you might enjoy thine exp_bin edges, sire: ",time.time()
    #gold_bin = gold.give_edges()
    print "Bonjour, cela sont ton gold_bin edges, monsieur: ", time.time()
    max_size = exp_bin.shape[0]
    print "Whao, that size is huge! ",time.time()
    poss = (max_size -1) * max_size 
    print "This shouldn't have taken any time"

    print "Gonna intersect that fish, check it out: ", time.time()
    isct = (exp_bin + gold_bin) / 2
    print "Intersected that fish, what up: ",time.time()
    isct = isct.astype(int)
    print "Made it an int, can't stop me now", time.time()
    #print isct
    #exp_sum  = float(sum(exp_bin.flatten().tolist()[0]))
    #gold_sum = float(sum(gold_bin.flatten().tolist()[0]))


    exp_sum  = float(len(exp_bin.nonzero()[0]))
    gold_sum = float(len(gold_bin.nonzero()[0]))
    isct_sum = float(len(isct.nonzero()[0]))
    print "Calculated those values like B-O-S-S: ",time.time()

    #print exp_sum
    #print gold_sum
    #print isct_sum
    #isct_sum = float(sum(isct.flatten().tolist()[0]))

    assert isct_sum != 0, "No overlap with gold standard"
    assert gold_sum != 0, "Gold standard is empty"
    assert isct_sum != exp_sum, "Experimental graph is gold standard"
    assert gold_sum != poss, "Gold standard is all possible edges"

    num = isct_sum / (exp_sum - isct_sum)
    den = gold_sum / (poss - gold_sum)

    LLS = log(num/den)
    print LLS
    return LLS

def WeightedSum(graph_list,gold):
    """Combine a list of [score,graph] data, sort, and collapse"""
    print 'In Weighted Sum ',time.time()
    gold_bin = gold.give_edges()
    forget = 1.8
    #score_graph_list = [[CompareGraphs(exp,gold_bin),exp.edges] for exp in graph_list]
    score_graph_list = sorted([[CompareGraphs(exp,gold_bin),exp.edges] for exp in graph_list],reverse=True,key=itemgetter(0))
    enum = [[i,j] for i,j in enumerate(score_graph_list)]
    norm = reduce(lambda x,y: x+y,map(lambda x: forget**(x[0]-1)*x[1][0],enum))
    ws = reduce(lambda x,y: x+y,map(lambda x: forget**(x[0]-1)*x[1][0]*x[1][1],enum))
    ws = ws / norm
    print "Hey man, did I do good?: ",time.time()
    with open("SA_3exp_test_eggNOG_2013-08-13.pkl",'w') as g:
        pickle.dump(ws,g)
    print "Dude, it's been real: ", time.time()
    return ws

if __name__ == "__main__":
    main()

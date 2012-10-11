import os
import sys
from pygraph.classes.digraph import digraph
from pygraph.algorithms import pagerank
import pickle


f=open('pr.graph','rb')
gr = pickle.load(f)
print gr
f.close()
pr=pagerank.pagerank(gr, max_iterations=500,min_delta=0.00001)
    
for k in pr:
  print k,pr[k]

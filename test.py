# Import the module and instantiate a graph object
from pygraph.classes.digraph import digraph
from pygraph.algorithms.searching import depth_first_search
from pygraph.algorithms import pagerank

gr = digraph()
# Add nodes
gr.add_nodes(['X','Y','Z'])
gr.add_nodes(['A','B','C'])
# Add edges
gr.add_edge(('X','Y'))
gr.add_edge(('X','Z'))
gr.add_edge(('A','B'))
gr.add_edge(('A','C'))
gr.add_edge(('Y','B'))
gr.add_edge(('X','B'))
# Depth first search rooted on node X
st, pre, post = depth_first_search(gr, root='X')
# Print the spanning tree
print st

print gr.incidents('B')

pr=pagerank.pagerank(gr,min_delta=0.0000001)
print pr

l=[]
for x in xrange(10000):
  l.append(x)

import sys
import types

def get_refcounts():
    d = {}
    sys.modules
    # collect all classes
    for m in sys.modules.values():
        for sym in dir(m):
            o = getattr (m, sym)
            if type(o) is types.ClassType:
                d[o] = sys.getrefcount (o)
    # sort by refcount
    pairs = map (lambda x: (x[1],x[0]), d.items())
    pairs.sort()
    pairs.reverse()
    return pairs

def print_top_100():
    for n, c in get_refcounts()[:100]:
        print '%10d %s' % (n, c.__name__)

if __name__ == '__main__':
    a=l
    print_top_100()

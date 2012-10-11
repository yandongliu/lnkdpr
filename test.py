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

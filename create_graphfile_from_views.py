import os
import sys
from pygraph.classes.digraph import digraph
from pygraph.algorithms.searching import depth_first_search
import pickle

view_dir='/home/ubuntu/linkedin/view/'

gr = digraph() 
cnt=0

def get_otherviewers(fn):
  rc=[]
  with open(fn,'r') as f:
    l=f.readline()
    #print l
    l=l.replace('http://','')
    owner,others=l.split('::::',1)
    #print 'owner:',owner
    others1=others.split(':::')
    for i in xrange(len(others1)/2):
      #print others1[i*2]
      #print others1[i*2].split('/')
      try:
        lnkdid=others1[i*2].split('/')[2]
        if '?' in lnkdid:
          lnkdid=lnkdid.split('?')[0]
        #print lnkdid
        rc.append(lnkdid)
      except Exception,ex:
        print 'ERROR!'
        print >> sys.stderr, fn
        print >> sys.stderr, others1
        print >> sys.stderr, i 
        print >> sys.stderr, ex
  return rc

added_nodes=set([])
added_edges=set([])
cnt=0

for subdir in os.listdir(view_dir):
  for subdir2 in os.listdir(view_dir+subdir):
    for fn in os.listdir(view_dir+subdir+'/'+subdir2):
      #print fn
      key=fn.split('__')[4]
      key=key.split('?')[0]
      #print fn.split('__')
      #print fn,key
      rc=get_otherviewers(view_dir+subdir+'/'+subdir2+'/'+fn)
      try:
        if key not in added_nodes:
          gr.add_node(key)
          added_nodes.add(key)
        for edg in rc:
          if edg not in added_nodes:
            gr.add_node(edg)
            added_nodes.add(edg)
          if (key,edg) not in added_edges:
            gr.add_edge((key,edg))
            added_edges.add((key,edg))
        cnt+=1
        #if cnt>100:break
      except Exception, ex:
        print 'graph ERROR:'
        print ex
        print fn
      cnt+=1
      #if cnt>10:sys.exit(1)
      if cnt%1000==0:
        print >>sys.stderr, 'processed %d files'%cnt

#print gr
f=open('pr.graph','wb')
pickle.dump(gr,f) 
f.close()

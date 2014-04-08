import sys
from collections import defaultdict

N=279725
if len(sys.argv)>1:
  N = float(sys.argv[1])
damp=0.15/N*2.0

score=defaultdict(float)
outgoing=defaultdict(list)
for l in sys.stdin:
  l = l.strip()
  data = l.split('\t')
  node=data[0]
  if data[1]=='p':
    score[node]+=float(data[2])
  if data[1]=='d':
    outgoing[node].append(data[2])

for node in score:
  sc=score[node]*0.85+damp
  print '%s\t%f\t%s'%(node,sc,'\t'.join(outgoing[node]))
    

#print score
#print outgoing

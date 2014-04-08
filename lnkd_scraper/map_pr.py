import sys

#input format:
#A pr(A) A1 A2 A3 ...

#output format
# A p pr(A) : pagerank score of A from one of A's incoming nodes
# A d A1: one of A's outoging edge A-> A1
for l in sys.stdin:
  l = l.strip()
  data = l.split('\t')
  if len(data)<=2:continue
  pr_each = float(data[1])/(len(data)-2)
  for n in data[2:]:
    print '%s\tp\t%f'%(n,pr_each)
  for n in data[2:]:
    print '%s\td\t%s'%(data[0],n)
  

import os
import sys

view_dir='view/'
#view_dir=sys.argv[1] 

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

for subdir in os.listdir(view_dir):
  for subdir2 in os.listdir(view_dir+subdir):
    for fn in os.listdir(view_dir+subdir+'/'+subdir2):
      #print subdir,subdir2,fn
      key=fn.split('__')[4]
      key=key.split('?')[0]
      #print fn.split('__')
      #print fn,key
      score=0.85
      try:
        rc=get_otherviewers(view_dir+subdir+'/'+subdir2+'/'+fn)
        if len(rc)<=0: continue
        #perscore=score/len(rc)
        #for neighbor in rc: 
        print '\t'.join([key,str(score),'\t'.join(rc)])
      except Exception,ex:
        print >>sys.stderr, ex
        print >>sys.stderr, subdir,subdir2,fn
      cnt+=1
      #if cnt>10:sys.exit(1)
      #if cnt%1000==0:
        #print >>sys.stderr, 'processed %d files'%cnt


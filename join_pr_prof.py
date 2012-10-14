import sys

fn_pr=sys.argv[1]
fn_prof=sys.argv[2]

x={}
current_id=''
profile={}
with open(fn_prof,'r') as f:
  for l in f:
    l=l.strip()
    if l.startswith('id:'):
      current_id=l.split(':')[1]
      profile={}
      x[current_id]=profile
    else:
      cols=l.split(':',1)
      profile[cols[0]]=cols[1]

#for c_id in x:
  #print c_id,x[c_id]
with open(fn_pr,'r') as f:
  cnt=0
  for l in f:
    cnt+=1
    l=l.strip()
    cols=l.split(' ')
    if cols[0] in x:
      p=x[cols[0]]
      id1=cols[0]
      print '%d\tid:%s\tname:%s\theadline:%s\tcurrent_pos:%s\tscore:%s'%(cnt,cols[0],p['name'],p['headline'],p['current position'],cols[1])
      #print 'id:<a href="data/%s/%s/%s">%s</a>\tname:%s\theadline:%s\tcurrent_pos:%s\tscore:%s'%(cols[0],p['name'],p['headline'],p['current position'],cols[1])
    else:
      print '%d\tid:%s\tname:%s\theadline:%s\tcurrent_pos:%s\tscore:%s'%(cnt,cols[0],'-','-','-',cols[1])

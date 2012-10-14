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
      cols=l.split(':')
      profile[cols[0]]=cols[1]

#for c_id in x:
  #print c_id,x[c_id]
with open(fn_pr,'r') as f:
  for l in f:
    l=l.strip()
    cols=l.split(' ')
    if cols[0] in x:
      p=x[cols[0]]
      print 'id:%s\tname:%s\theadline:%s\tcurrent_pos:%s\t%s\tscore:%s'%(cols[0],p['name'],p['headline'],p['current position'],p['companies'],cols[1])
    else:
      print 'id:%s\tname:%s\theadline:%s\tcurrent_pos:%s\t%s\tscore:%s'%(cols[0],'-','-','-','-',cols[1])

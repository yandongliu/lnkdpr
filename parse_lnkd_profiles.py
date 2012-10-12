import sys
import re
import os

def parse(fn):
  name=None
  headline=None
  current_pos=None
  with open(fn,'r') as f:
    content=f.read()

    m=p_headline.findall(content)
    if m:
      headline= m[0].strip()

    m=p_name.findall(content)
    if m:
      name= (m[0][0]+' '+m[0][1]).strip()

    m=p_current.findall(content)
    if m:
      current=p_tag.sub('',m[0].replace('\n',' '))
      current_pos=current.replace('  ',' ').strip()
  return name,headline,current_pos
    
p_headline=re.compile('<p class="headline-title title" style="display:block">(.*?)</p>',re.MULTILINE|re.DOTALL)
p_name=re.compile('<span class="full-name"><span class="given-name">(.*?)</span> <span class="family-name">(.*?)</span></span>')
p_current=re.compile('<ul class="current">\n*<li>(.*?)\n*</li>',re.MULTILINE|re.DOTALL)
str_current='<ul class="current">\n*<li>(.*?)\n*</li>'
p_tag = re.compile(r'<[^>]+>')
data_dir='/home/ubuntu/linkedin/data/'
#view_dir='./view/'

cnt=0

for subdir in os.listdir(data_dir):
  for fn in os.listdir(data_dir+subdir):
    name,hl,current_pos=parse(data_dir+subdir+'/'+fn)
    print 'id:%s'%fn.split('__')[4].split('?')[0]
    print 'name:%s'%name
    print 'headline:%s'%hl
    print 'current position:%s'%current_pos
    cnt+=1
    if cnt%1000==0:
      print >>sys.stderr, 'processed %d profiles'%cnt

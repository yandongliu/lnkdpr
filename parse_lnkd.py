import sys
import re
import os

def get_title(fn):
  #print 'file:'+fn
  name=None
  headline=None
  current_pos=None
  with open(fn,'r') as f:
    content=f.read()
    #print content

    m=p_headline.findall(content)
    #print m
    if m:
      headline= m[0].strip()

    m=p_name.findall(content)
    #print m
    if m:
      name= (m[0][0]+' '+m[0][1]).strip()

    m=p_current.findall(content)
    if m:
      #current=m[0]
      #print 'CURRENT1:',m
      #print 'CURRENT1:',m
      #print 'CURRENT:',m[0].replace('\n',' ')
      current=p_tag.sub('',m[0].replace('\n',' '))
      current_pos=current.replace('  ',' ').strip()
      #print 'CURRENT:',current
      #jprint 'CURRENT:',current
  return name,headline,current_pos
    
p_headline=re.compile('<p class="headline-title title" style="display:block">(.*?)</p>',re.MULTILINE|re.DOTALL)
p_name=re.compile('<span class="full-name"><span class="given-name">(.*?)</span> <span class="family-name">(.*?)</span></span>')
p_current=re.compile('<ul class="current">\n*<li>(.*?)\n*</li>',re.MULTILINE|re.DOTALL)
str_current='<ul class="current">\n*<li>(.*?)\n*</li>'
p_tag = re.compile(r'<[^>]+>')
data_dir='/home/ubuntu/linkedin/data/'
view_dir='./view/'

for subdir in os.listdir(data_dir):
  for fn in os.listdir(data_dir+subdir):
    name,hl,current_pos=get_title(data_dir+subdir+'/'+fn)
    print 'id:%s'%fn.split('__')[4].split('?')[0]
    print 'name:%s'%name
    print 'headline:%s'%hl
    print 'current position:%s'%current_pos

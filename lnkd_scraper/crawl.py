#!/usr/bin/env python

import sys
import re
import mechanize 
import cookielib
import os.path
import os
import time
import random
import Queue
import gc
from mechanize import ParseResponse, urlopen, urljoin

data_dir='./data/'
view_dir='./view/'
p_otherview=re.compile('<li class="with-photo">.*?<strong>.*?<a href="([^"]+)">(.*?)</a>', re.MULTILINE|re.DOTALL)

def get_url_storekey_l1(uri): 
  subdir=uri.replace('/','__').split('__')[4][:2]
  return subdir+'/'

def get_url_storekey_l2(uri): 
  subdir=uri.replace('/','__').split('__')[4][:3]
  return subdir+'/'

def ensure_dir(dir1):
  if not os.path.exists(dir1):
    os.mkdir(dir1)

def save_otherviews(name,url,links):
  fn=url.replace('/','__')
  print >>sys.stderr, 'writing to view dir:', view_dir,get_url_storekey_l1(url),get_url_storekey_l2(url),fn
  ensure_dir(view_dir+get_url_storekey_l1(url))
  ensure_dir(view_dir+get_url_storekey_l1(url)+get_url_storekey_l2(url))
  f=open(view_dir+get_url_storekey_l1(url)+get_url_storekey_l2(url)+fn,'w')
  ls=[]
  for link in links:
    ls.append(link[0])
    ls.append(link[1])
  str= name+','+url+'::::'+':::'.join(ls)
  str=str.encode('ascii', 'ignore')
  f.write(str)
  f.close()

def save_to_file(fn,content):
  print >>sys.stderr, 'writing to view dir:', data_dir,get_url_storekey_l1(url),get_url_storekey_l2(url),fn
  ensure_dir(data_dir+get_url_storekey_l1(fn))
  ensure_dir(data_dir+get_url_storekey_l1(fn)+get_url_storekey_l2(url))
  f=open(data_dir+get_url_storekey_l1(fn)+get_url_storekey_l2(url)+fn,'w')
  #content=content.encode('ascii', 'ignore')
  f.write(content)
  f.close()

def download_url(url,links_crawled,cj): 
  if os.path.isfile(fn_linkedcookie):
    cj.revert(fn_linkedcookie)
  print 'downloading link:'+url
  #global links_crawled
  links_crawled.add(url)
  br=get_browser()
  r=br.open(url) 
  #print r
  #print r.info()
  html= r.read() 
  cj.save(fn_linkedcookie)
  br.close()
  del br
  return html

  
def get_links(html):
  l=[]
  m=p_otherview.findall(html)
  if m:
    for g in m:
      l.append((g[0],g[1]))
  else:
    print "---didnt find"
  return l
  

def get_links2(html):
  soup = BeautifulSoup(html) 
  lis=soup.find_all("li", class_="with-photo")
  links=[]
  for li in lis:
    #print li.find_all('a')[1]
    print li.find_all('a')[1]['href'], li.find_all('a')[1].string
    links.append((li.find_all('a')[1]['href'],li.find_all('a')[1].string))
  del soup
  return links

def if_data_saved(url):
  subdir=get_url_storekey_l1(url)+get_url_storekey_l2(url)
  if os.path.isfile(data_dir+subdir+url.replace('/','__')):
    return True
  else: return False

def if_view_saved(url):
  subdir=get_url_storekey_l1(url)+get_url_storekey_l2(url)
  if os.path.isfile(view_dir+subdir+url.replace('/','__')):
    return True
  else: return False

def read_existing_data_saved(set1):
  for subdir in os.listdir(data_dir):
    set1.update(os.listdir(data_dir+subdir))

def read_existing_view_saved():
  for subdir in os.listdir(view_dir):
    views_crawled.update(os.listdir(view_dir+subdir))

def read_tocrawl_links(q):
  with open('tocrawl.txt','r') as f:
    for l in f:  
      try:
        name,url=l.strip().split('\t') 
        q.put((url,name))
      except Exception,ex:
        print l
        print ex

def save_tocrawl_links(q):
  q2=Queue.Queue()
  with open('tocrawl.txt','w') as f:
    while not q.empty():
      url,name = q.get()
      q2.put((url,name))
      name=name.encode('ascii', 'ignore')
      f.write(name+'\t'+url+'\n')
  return q2
    
  

def get_browser():
  br = mechanize.Browser()
  br.set_handle_robots(False) 
  br.set_cookiejar(cj) 
  br.set_handle_equiv(True)
  br.set_handle_gzip(True)
  br.set_handle_redirect(True)
  br.set_handle_referer(True)
  br.set_handle_robots(False)
  # Follows refresh 0 but not hangs on refresh > 0
  br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
  br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
  return br


links_crawled=set([])
views_crawled=set([])
q=Queue.Queue()

uri = "http://www.linkedin.com/in/marissamayer" 
#uri = "http://www.linkedin.com/pub/ken-delaney/5/2a9/65b?trk=pub-pbmap" 
uri = "http://www.linkedin.com/pub/sean-parker/0/1/826" 

fn_linkedcookie='cookie_linkedin_nologin.txt'
cj = cookielib.LWPCookieJar() 

#links_crawled.update(os.listdir("./data"))
read_existing_data_saved(links_crawled)
print 'has downloaded links:', len(links_crawled)
#read_existing_view_saved()
print 'has downloaded view profiles:', len(views_crawled)
read_tocrawl_links(q)

#html=download_url(br,uri)

#links=get_links(html)
#save_otherviews('name',uri,links)
#for link in links:
  #q.put(link)

save_tocrawl_cnt=0
gc_cnt=0

while not q.empty():
  url,name=q.get()
  if url.replace('/','__') in links_crawled:
    print 'Skipping cache: ',url
    continue
  elif if_data_saved(url):
    print 'Skipping disk: ',url
    continue
  html=''
  print 'to crawl link queue size:',q.qsize()
  print 'crawled linked size:',len(links_crawled)
  print 'crawled views size:',len(views_crawled)
  try:
    html=download_url(url,links_crawled,cj)
  except Exception,ex:
    print ex
    continue
  links_crawled.add(url.replace('/','__'))
  if len(links_crawled)>10000:
    print 'clearing links_crawled'
    links_crawled.clear()
  if len(views_crawled)>10000:
    print 'clearing views_crawled'
    views_crawled.clear()
  save_to_file(url.replace('/','__'),html)
  print 'sleeping...'
  time.sleep(random.randint(10,20))
  links=get_links(html)
  save_otherviews(name,url,links)
  if q.qsize()<100000:
    for link in links:
      if link[0].replace('/','__') in links_crawled:
        print 'Skipping cache: ',url
        continue
      elif if_data_saved(link[0]):
        print 'Skipping disk: ',url
        continue
      q.put(link)
  del links
  save_tocrawl_cnt+=1
  if save_tocrawl_cnt==10:
    print 'saving to crawl links'
    q=save_tocrawl_links(q)
    save_tocrawl_cnt=0
  gc_cnt+=1
  print 'gc:',gc_cnt
  if gc_cnt>=100:
    print '======GC======',gc.collect()
    gc_cnt=0

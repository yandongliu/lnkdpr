import os
import shutil

dir_data="./data/"
dir_data="./view/"
s=set([])
s.update(os.listdir(dir_data))

for uri in s:
  #print uri , uri.split('__')[4]
  subdir=uri.split('__')[4][:2]
  if not os.path.exists(dir_data+subdir):
    os.mkdir(dir_data+subdir)
  print 'moving '+uri
  shutil.move(dir_data+uri,dir_data+subdir+'/'+uri)

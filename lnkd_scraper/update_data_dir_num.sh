for x in `ls data`; do echo -n $x" "; find data/$x|wc -l; done|sort -grk2 > data_dir_profnum.txt

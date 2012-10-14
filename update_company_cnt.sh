 cut -f5 joined.txt |awk 'BEGIN{FS=":"}{for( i=2;i<NF;i++) print $i}'|sort|uniq -c|sort -grk1 > companies.txt

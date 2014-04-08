for i in $(seq 100)
do
  input=$i
  output=`expr $i + 1`
  echo iter,$input
  n=`wc -l iter${input}.txt|cut -f1 -d" "`
  echo $n
  echo cat iter${input}.txt \|python map_pr.py \|python red_pr.py $n  iter${output}.txt
  cat iter${input}.txt |python map_pr.py |python red_pr.py $n > iter${output}.txt
done

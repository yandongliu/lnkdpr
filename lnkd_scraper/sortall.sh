for i in $(seq 100)
do
  sort -grk2 iter${i}.txt > sorted/iter${i}.txt
done

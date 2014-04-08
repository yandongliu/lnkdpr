hstream='hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.2.jar -D mapred.output.compress=true -D mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec'


input_path=/projects/science/input/yandong/tmp/
output_path=/projects/science/input/yandong/tmp_output/


echo $hstream -input "$input_path" -output ${output_path} -mapper 'python map_pr.py' -file map_pr.py -reducer 'python red_pr.py' -file red_pr.py -jobconf mapred.reduce.tasks=50
$hstream -input "$input_path" -output ${output_path} -mapper 'python map_pr.py 279725' -file map_pr.py -reducer 'python red_pr.py' -file red_pr.py -jobconf mapred.reduce.tasks=50

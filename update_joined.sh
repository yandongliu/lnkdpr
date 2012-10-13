git pull
python pr_from_graph_pickle.py|sort -grk2 > pr.txt
python join_pr_prof.py pr.txt profiles.txt > joined.txt

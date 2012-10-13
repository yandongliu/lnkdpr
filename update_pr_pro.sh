echo pr.graph
python create_graphfile_from_views.py 
echo profiles.txt
python parse_lnkd_profiles.py > profiles.txt
git add pr.graph
git add profiles.txt
git commit -m "updated pr.graph profiles.txt"
git push


::del .\results\*.* 
::rmdir results
::#mkdir results
python getnextpage.py > results/pages.txt
python bepis.py 
python Listofitemlinks.py > results/itemlinks.txt
python remove_duplicates.py --path "./results/itemlinks.txt" > "./results/itemlinks_nodupe.txt"
python genfiles.py > "./results/einfo.txt"

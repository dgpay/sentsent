from more_itertools import unique_everseen
with open('file2-next.csv','r') as f, open('akhirpisan.csv','w') as out_file:
    out_file.writelines(unique_everseen(f))
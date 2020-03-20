from more_itertools import unique_everseen
with open('train andai - Sheet1.csv','r') as f, open('train andai - Sheet11','w') as out_file:
    out_file.writelines(unique_everseen(f))
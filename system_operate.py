import os
import shutil

fout = open('oops.txt', 'wt')
print('Oops, I created a file.', file=fout)
fout.close()

os.path.exists('oops.txt')
name = 'oops.txt'
os.path.isfile(name)
os.path.isdir(name)
os.path.isabs(name)

shutil.copy('oops.txt', 'ohno.txt ')
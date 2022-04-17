import os

from glob import iglob

from os.path import isfile

f = [i for i in iglob(f"{os.getcwd()}//**", recursive=True) if isfile(i)]

for i in f: print(i)

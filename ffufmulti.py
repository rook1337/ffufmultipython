import os
import sys
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
folder=sys.argv[1]
file1 = open(folder+"/"+"status.txt", 'r')
Lines = file1.readlines()
urlcount=len(Lines)
num=0
for line in Lines:
    num=num+1
    os.system("~/go/bin/ffuf -w autorecon/myword.txt  -u "+str.strip(line)+"/FUZZ -recursion -recursion-depth 2 -mc 200 -ac -o ffufout"+str(num)+".txt")

dirs=""
for x in range(urlcount):
    x=x+1
    outfile="ffufout"+str(x)+".txt"
    f = open(outfile)
    data = json.load(f)
    for i in range(len(data['results'])):
        dirs=dirs+data['results'][i]['url']+"\n"

    f.close()
    file1 = open(folder+"/dirs.txt","a")
    file1.write(dirs)
    file1.close()
    os.system("rm -rf ffufout"+str(x)+".txt")
#!/usr/bin/env python
# encoding: utf-8

#在ipython notebook上探索 ，很爽！
#oc-srt-1427970012101.srt 中文
#oc-srt-1427970019939.srt 英文
with open("oc-srt-1427970012101.srt") as f:
    lines1 = f.readlines() #中文
print lines1 #4400
with open("oc-srt-1427970019939.srt") as f:
    lines2 = f.readlines() #英文
#print lines2 #4400
chineses = [value for (index, value) in enumerate(lines1) if (index-2)%4==0]
print len(chineses) #1100

new_lines=[]
new_lines=[]
j = 0
for (index, value) in enumerate(lines2):
    new_lines.append(value)
    if  (index-1)%4==0:
        #print (index,value)
        new_lines.append(chineses[j])
        j=j+1
with open("ok.txt","w") as out:
    out.writelines(new_lines)

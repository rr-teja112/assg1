s=input()
o=''
for i in s:
    if i.isdigit():
        o+=i
o=set(o)        
for i in o:
      print(i,end='')        
        

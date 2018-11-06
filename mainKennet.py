located_map="TeamOntspoord"

<<<<<<< HEAD
for name in nameList:
    if name=="Kennet":
        print(name,",dat is een mooie naam!! Er mist alleen een h")
    else:
        print(name,",hmmm")
=======
import os, sys
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name+"\\"+located_map+"\\code")
>>>>>>> fe25b44bd13f7475eb1136f609ee03469a8791b3


print(parent_dir_name)
print(parent_dir_name+"\\"+located_map+"\\code" )


import network as nw

nw.import_other_func()

located_map="TeamOntspoord"

import os, sys
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name+"\\"+located_map+"\\code")


print(parent_dir_name)
print(parent_dir_name+"\\"+located_map+"\\code" )


import network as nw

nw.import_other_func()

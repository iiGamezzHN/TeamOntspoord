def ndict(graph,all_nodes,dict,step):
    list=[]
    for x in dict[step]:
        for y in graph[x]:
            if y not in all_nodes:
                list.append(y)
                all_nodes.append(y)
                dict[step+1]=list
    step += 1
    return all_nodes,dict,step

def pathcount(graph,node,nrange):
	dict={}
	all_nodes=[node]
	dict[0]=[node]
	step=0
	for step in range(nrange):
		if step==nrange-1:
			return dict
		if dict[step]==[]:
			return dict
		else:
			ndict(graph,all_nodes,dict,step)

def pathmaker(graph,bfs):
	parent_children=[]
	lenght= len(bfs)
	for i in range(lenght-1):
		for parent in bfs[i]:
			for child in bfs[i+1]:
				if child in graph[parent]:
					parent_children.append([parent,child])
	return parent_children

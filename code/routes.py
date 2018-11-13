import copy

def timelimit(graph,track):
	track_time=0
	for i in range(len(track)):
		if i+1<len(track):
			a= track[i]
			b= track[i+1]
			time= float(graph[a][b]['weight'])
			track_time+= time
	return track_time

def all_shortest_nodes(graph,station,limit):
	begin=bfs.pathcount(graph,station,20)
	list1=[x for x in bfs.pathmaker(graph,begin)]
	list2=[x for x in bfs.pathmaker(graph,begin)]
	list3=[]
	for x in list1:
		l_index=len(x)-1
		first=x[:l_index]
		second=x[l_index:]
		for y in list2:
			if y[0] == second[0]:
				new_c=first+y
				list1.append(new_c)
	for x in list1:
		if x[0]==station and timelimit(graph,x)<=limit:
			list3.append(x)
	return list3

def combine_all_timelimit(graph,station,limit):
	""" Get all possible tracks from the input station to all the other stations in
	network. Be cautious using the timelimit. Using 'Utrecht Centraal' and a limit
	of 180 minutes can cause runtimes of 10 minutes """
	finallist= all_shortest_nodes(graph,station,limit)
	templist= copy.copy(finallist)
	i=0
	for x in templist:
		last= x[len(x)-1:]
		for y in all_shortest_nodes(graph,last[0],120):
			new=x+y[1:]
			if timelimit(graph,new)<=limit:
				if y[0]!=station and y[1]!=station and len([l for l in y[1:] if l in x])==0:
					if new not in templist:
						templist.append(new)
						i+=1
						print(i,timelimit(graph,new),new)
	limit=[x for x in templist if timelimit(graph,x)<=limit]
	return limit

def shortest_routes(graph,station_a,station_b,limit):
	all_routes= combine_all_timelimit(graph,station_a,limit)
	a_b_routes=[]
	for x in all_routes:
		if x[0]==station_a and x[len(x)-1]==station_b:
			a_b_routes.append([timelimit(graph,x),x])
	return sorted(a_b_routes,key=lambda x: x[0])

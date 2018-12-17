import generate_tracks as gt
import score as sc
import transform_tracklist as tt



import matplotlib.pyplot as plt
from collections import Counter
import operator
from random import randint
import copy



""" ['random',20,180,apct,uct] """

def histo(graph,option):
	colors=['yellow','red','blue','black','green']
	solution_dict={}
	if option[0]=='random':
		print('random')
		nr_t 	=option[1]
		limit	=option[2]
		apct	=option[3]
		uct 	=option[4]

		bins=[x*50 for x in range(200)]
		for t in nr_t:
			h_score=0
			histo_list=[]

			data=[]
			for i in range(500):
				tracks= gt.tracksRandom(graph,t,limit)
				tt.transform(graph,tracks)
				score=sc.score(graph,tracks,apct,uct)[0]

				data.append(round(score,0))
				histo_list.append([i,score])
				if score>h_score:
					h_score=score
					end=tracks
					print(t,i,score)
			solution_dict[t]=[h_score,end]
			count_data=Counter(data)
			sorted_data = sorted(count_data.items(), key=operator.itemgetter(0))
			x_axis=[x[0] for x in sorted_data]
			y_axis=[x[1] for x in sorted_data]

			plt.plot(x_axis, y_axis, '-',color=colors[nr_t.index(t)])
			plt.hist(data, bins=bins,color=colors[nr_t.index(t)], range=None, density=None, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, label=None, stacked=False, normed=None, hold=None, data=None)
		plt.show()
	elif option[0]=='greedy':
		print('greedy')
		nr_t 	=option[1]
		limit	=option[2]
		apct	=option[3]
		uct 	=option[4]

		bins=[x*50 for x in range(200)]
		for t in nr_t:
			h_score=0
			histo_list=[]

			data=[]
			for i in range(500):
				tracks= gt.tracksRandom(graph,t-1,limit)
				all_stations= [x for x in graph.nodes()]
				last_station= all_stations[randint(0,len(all_stations)-1)]
				all_station_tracks= hd.holland_dict[last_station]
				g_score=0
				for s in all_station_tracks:
					temp_tracks= copy.copy(tracks)
					temp_tracks.append(s)
					tt.transform(graph,tracks)
					score=sc.score(graph,temp_tracks,apct,uct)[0]
					if score>g_score:
						g_score=score
						temp_end=temp_tracks
				score=g_score

				data.append(round(score,0))
				histo_list.append([i,score])
				if score>h_score:
					h_score=score
					end=temp_end
					print(t,i,score)
			solution_dict[t]=[h_score,end]
			count_data=Counter(data)
			sorted_data = sorted(count_data.items(), key=operator.itemgetter(0))
			x_axis=[x[0] for x in sorted_data]
			y_axis=[x[1] for x in sorted_data]

			plt.plot(x_axis, y_axis, '-',color=colors[nr_t.index(t)])
			plt.hist(data, bins=bins,color=colors[nr_t.index(t)], range=None, density=None, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, label=None, stacked=False, normed=None, hold=None, data=None)

		plt.show()

	elif option[0]=='super greedy':
		print('super greedy')
		nr_t 	=option[1]
		limit	=option[2]
		apct	=option[3]
		uct 	=option[4]

		bins=[x*50 for x in range(200)]
		for t in nr_t:
			h_score=0
			histo_list=[]

			data=[]
			for i in range(10):
				tracks= []
				all_stations= [x for x in graph.nodes()]
				for i in range(t):
					last_station= all_stations[randint(0,len(all_stations)-1)]
					all_station_tracks= hd.holland_dict[last_station]
					g_score=0
					for s in all_station_tracks:
						temp_tracks= copy.copy(tracks)
						temp_tracks.append(s)
						tt.transform(graph,tracks)
						score=sc.score(graph,temp_tracks,apct,uct)[0]
						if score>g_score:
							g_score=score
							temp_end=temp_tracks
					score=g_score
					tracks=temp_end

				data.append(round(score,0))
				histo_list.append([i,score])
				if score>h_score:
					h_score=score
					end=temp_end
					print(t,i,score)
			solution_dict[t]=[h_score,end]
			count_data=Counter(data)
			sorted_data = sorted(count_data.items(), key=operator.itemgetter(0))
			x_axis=[x[0] for x in sorted_data]
			y_axis=[x[1] for x in sorted_data]

			plt.plot(x_axis, y_axis, '-',color=colors[nr_t.index(t)])
			plt.hist(data, bins=bins,color=colors[nr_t.index(t)], range=None, density=None, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, label=None, stacked=False, normed=None, hold=None, data=None)

		plt.show()
	return solution_dict

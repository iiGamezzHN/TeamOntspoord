import matplotlib.pyplot as plt
import networkx as nx
import gc
import decimal



def import_other_func():
    """
    This function is purely made to test whether the main.py can succesfully import other functions
    from the folder 'code' and use them.
    """
    print("It's working")


class Network_Graph():
    """docstring for ClassName"""

    def __init__(self, station_class):

        """ Deze init heeft een class als input, in ons geval gaat het hier om de class Station. De init zal
        aan de hand van deze class een netwerk opbouwen mbv networkx. Het netwerk bevat de stations als nodes,
        de verbindingen tussen stations als edges en de reistijd als weight van de edges. """

        self.station_class = station_class
        # create l of instances of class Station by looping through all objects
        stations = [obj.name for obj in gc.get_objects() if isinstance(obj,
                    station_class)]
        # https://stackoverflow.com/questions/328851/printing-all-instances-of-a-class
        double_connections = [(obj.name, n[0], n[1]) for obj in gc.get_objects() if isinstance(obj, station_class) for n in obj.neighbours]
        locations = [(obj.name, obj.location) for obj in gc.get_objects() if isinstance(obj, station_class)]
        node_loc_dict = {x[0]: x[1] for x in locations}
        labels = {obj.name: obj.label for obj in gc.get_objects() if isinstance(obj, self.station_class)}

        self.graph = nx.Graph()
        self.graph.add_nodes_from(stations)

        for a, b, w in double_connections:
            if self.graph.has_edge(a, b) is False:
                self.graph.add_edge(a, b, weight=w)
        for n, p in locations:
            self.graph.node[n]['pos'] = p

        c_list = [obj.name for obj in gc.get_objects() if isinstance(obj, self.station_class) if obj.importance == 'Kritiek']
        nc_list = [obj.name for obj in gc.get_objects() if isinstance(obj, self.station_class) if obj.importance != 'Kritiek']

    def information(self):
        """Returns the amount of nodes and the nodes themselves """
        return '{} {} {} {} {}'.format('There are', len(self.graph.nodes()), 'nodes', '\nNodes:', self.graph.nodes())

    def calc_statespace(self,option):
        if option == 'Holland':
            minutes = 120
            max_t = 7
        if option == 'Nationaal':
            minutes = 180
            max_t = 20
        tot_nodes = len(self.graph.nodes())
        tot = 0
        min_w = []
        for node in self.graph.nodes():
            n = len([x for x in self.graph[node]])
            w = min([int(float(self.graph[node][x]['weight'])) for x in self.graph[node]])
            min_w.append(w)
            if n > tot:
                tot = n
        min_w = min(min_w)
        max_c = minutes/min_w
        statespace = 0
        track_statespace = decimal.Decimal(tot_nodes*(tot**max_c)/2)
        for t in range(1, max_t+1):
            statespace = decimal.Decimal(statespace+track_statespace**t)
            # print(t, tot_nodes, tot, max_c, track_statespace, decimal.Decimal(track_statespace**t), statespace)

        return '{} {} {} {} {} {} {} {} {} {} {}'.format('There are', tot_nodes, 'nodes',
                    '\nThe most amount neighbours of a node is', tot,
                    '\nMinimal time between nodes is', min_w,
                    '\nStatespace of a single track x is', track_statespace,
                    '\nTotal statespace is', statespace)


    def draw_choice(self, option, egdes_option):
        """ This functions will create a visualisation of the graph. The input is the option to
        chose which stations to show.
        standard= a graph with all the stations
        critical= a graph with only the critical stations
        track= a graph with only the stations from the track and critical stations
        tracks= shows a graph, all the critical edges are blue, the remaining critical edges are red
        The second input is the edges_option, if its true all the edge labels will show
        """
        graphdict = {}
        locations = [(obj.name, obj.location) for obj in gc.get_objects() if isinstance(obj, self.station_class)]
        graphdict = {x[0]: x[1] for x in locations}

        c_list = [obj.name for obj in gc.get_objects() if isinstance(obj, self.station_class) if obj.importance=='critical']
        nc_list = [obj.name for obj in gc.get_objects() if isinstance(obj, self.station_class) if obj.importance=='not critical']

        nx.draw(self.graph, graphdict, font_size=8, node_size=1, edge_width=0.1, width=0.1)
        nx.draw_networkx_nodes(self.graph, graphdict, node_size=30, nodelist=c_list, node_color='lightsalmon')
        nx.draw_networkx_nodes(self.graph, graphdict, node_size=20, nodelist=nc_list, node_color='lightgrey')

        if option == 'standard':
            labels = {obj.name: obj.label for obj in gc.get_objects() if isinstance(obj, self.station_class)}
        elif option == 'critical':
            labels = {obj.name: obj.label for obj in gc.get_objects() if isinstance(obj, self.station_class) if obj.importance=='critical'}
        elif option[0] == 'track':
            tracks = option[1]
            for x in tracks:
                track = x[0]
                time = x[1]
                templist = []
                edge_labels = {}
                for y in track:
                    templist.append(y[0][0])
                    templist.append(y[0][1])
                    edge_labels[(y[0][0],y[0][1])]=y[1]
                tracklist = set(templist)
                t_labels = {obj.name: obj.label for obj in gc.get_objects() if isinstance(obj, self.station_class) if obj.name in tracklist}
                r_labels = {obj.name: obj.label for obj in gc.get_objects() if isinstance(obj, self.station_class) if obj.importance == 'critical' and obj.name not in t_labels}

                nx.draw(self.graph, graphdict, font_size=8, node_size=1, edge_width=0.1, width=0.1)
                nx.draw_networkx_nodes(self.graph, graphdict, node_size=30, nodelist=c_list, node_color='lightsalmon')
                nx.draw_networkx_nodes(self.graph, graphdict, node_size=20, nodelist=nc_list, node_color='lightgrey')

                nx.draw_networkx_edges(self.graph, graphdict, edgelist=edge_labels, width=0.5, edge_color='blue', style='solid', with_label=True)
                nx.draw_networkx_edge_labels(self.graph, graphdict, edge_labels=edge_labels, font_size=6)
                nx.draw_networkx_labels(self.graph, graphdict, t_labels, font_size=8, font_weight='bold')
                nx.draw_networkx_labels(self.graph, graphdict, r_labels, font_size=8, font_weight='normal')
                plt.show(self.graph)

        elif option[0] == 'all tracks':
            tracks = option[1]
            templist = []
            edge_labels = {}
            for x in tracks:
                track = x[0]
                time = x[1]
                for y in track:
                    templist.append(y[0][0])
                    templist.append(y[0][1])
                    edge_labels[(y[0][0], y[0][1])] = y[1]
            tracklist = set(templist)
            t_labels = {obj.name: obj.label for obj in gc.get_objects() if isinstance(obj, self.station_class) if obj.name in tracklist}
            r_labels = {obj.name: obj.label for obj in gc.get_objects() if isinstance(obj, self.station_class) if obj.importance == 'critical' and obj.name not in t_labels}
            b_labels = {obj.name: obj.label for obj in gc.get_objects() if isinstance(obj, self.station_class) if obj.importance == 'critical'}

            nx.draw(self.graph, graphdict, font_size=8, node_size=1, edge_width=0.1, width=0.1)
            nx.draw_networkx_nodes(self.graph, graphdict, node_size=30, nodelist=c_list, node_color='lightsalmon')
            nx.draw_networkx_nodes(self.graph, graphdict, node_size=20, nodelist=nc_list, node_color='lightgrey')

            # draw every critical edge red (if the track covers this edge it will become blue)
            critical_labels = {(x[0][0], x[0][1]) :x[1] for x in option[2]}
            red_labels = {x: critical_labels[x] for x in critical_labels if x not in edge_labels and (x[1], x[0]) not in edge_labels}
            print(red_labels)

            nx.draw_networkx_edges(self.graph, graphdict, edgelist=red_labels,width=1, edge_color='red', style='solid', with_label=True)

            nx.draw_networkx_edges(self.graph, graphdict, edgelist=edge_labels,width=0.5, edge_color='blue', style='solid', with_label=True)
            # nx.draw_networkx_edge_labels(self.graph, graphdict,edge_labels=edge_labels,font_size=6)
            nx.draw_networkx_labels(self.graph, graphdict, b_labels, font_size=8, font_weight='bold')
            # nx.draw_networkx_labels(self.graph,graphdict,t_labels,font_size=8,font_weight='bold')
            # nx.draw_networkx_labels(self.graph,graphdict,r_labels,font_size=8,font_weight='normal')
            plt.show(self.graph)

        if 'labels' in locals():
            # runs these lines if you use 'standard' or 'critical' since you've
            # created the variable labels
            nx.draw_networkx_labels(self.graph, graphdict, labels, font_size=8, font_weight='normal')
            edge_labels = nx.get_edge_attributes(self.graph, 'weight')
            nx.draw_networkx_edges(self.graph, graphdict, edge_labels=edge_labels, width=0.1, edge_color='k', style='solid')
            if egdes_option == True:
                nx.draw_networkx_edge_labels(self.graph, graphdict, edge_labels=edge_labels, font_size=6)
            plt.show(self.graph)

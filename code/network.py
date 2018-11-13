import matplotlib.pyplot as plt
import networkx as nx
import gc



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
        #create list of instances of the class Station by looping through all objects
        stations= [obj.name for obj in gc.get_objects() if isinstance(obj, station_class)]   #https://stackoverflow.com/questions/328851/printing-all-instances-of-a-class
        double_connections= [(obj.name,n[0],n[1]) for obj in gc.get_objects() if isinstance(obj, station_class) for n in obj.neighbours]
        locations= [(obj.name,obj.location) for obj in gc.get_objects() if isinstance(obj, station_class)]
        node_loc_dict= {x[0]:x[1] for x in locations}
        labels= {obj.name:obj.label for obj in gc.get_objects() if isinstance(obj, self.station_class)}

        self.graph = nx.Graph()
        self.graph.add_nodes_from(stations)


        for a,b,w in double_connections:
            if self.graph.has_edge(a,b)==False:
                self.graph.add_edge(a,b, weight=w)
        for n,p in locations:
            self.graph.node[n]['pos']=p

        c_list= [obj.name for obj in gc.get_objects() if isinstance(obj, self.station_class) if obj.importance=='Kritiek']
        nc_list= [obj.name for obj in gc.get_objects() if isinstance(obj, self.station_class) if obj.importance!='Kritiek']

        nx.draw(self.graph, node_loc_dict,font_size=8,node_size=1,edge_width=0.1,width=0.1)
        nx.draw_networkx_nodes(self.graph,node_loc_dict,node_size=30,nodelist=c_list,node_color='lightsalmon')
        nx.draw_networkx_nodes(self.graph,node_loc_dict,node_size=20,nodelist=nc_list,node_color='lightgrey')

        nx.draw_networkx_labels(self.graph,node_loc_dict,labels,font_size=8,font_weight='normal')
        edge_labels = nx.get_edge_attributes(self.graph,'weight')
        nx.draw_networkx_edges(self.graph, node_loc_dict, edge_labels=edge_labels, width=0.1, edge_color='k', style='solid')
        nx.draw_networkx_edge_labels(self.graph, node_loc_dict,edge_labels=edge_labels,font_size=6)

    def plot_graph(self):
        plt.show(self.graph)

    def information(self):
        """Returns the amount of nodes and the nodes themselves """
        return '{} {} {} {} {}'.format('There are',len(self.graph.nodes()),'nodes','\nNodes:',self.graph.nodes())

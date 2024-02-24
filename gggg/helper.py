import math
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def euclidean_distance(coord1, coord2):
    dis = math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)
    return dis


def count_clusters(graph):
    return len(list(nx.connected_components(graph)))


def cusrandis(k  , maxdis):
    windowsize = max(maxdis - k +1 , 1)
    lpp = np.random.laplace(0,windowsize ** 0.1 )
    lpp = int(k + (abs(lpp))%windowsize)

    return lpp

def graphify(graph , to_plot):
    # pos = {i: coord for coord, i in cordmap.items()}
    if not to_plot :
        return
        
    pos = nx.get_node_attributes(graph, "pos")
    nx.draw(
        graph,
        pos,
        with_labels=True,
        font_weight="bold",
        node_color="lightgreen",
        font_size=10,
        node_size=700,
    )
    plt.show()

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._aereporti = DAO.getAllAirports()
        self._idMapAP = {}
        for a in self._aereporti:
            self._idMapAP[a.ID] = a

    def buildGraph(self,x):
        self._graph.clear()
        nodi = DAO.getAllNodes(x)
        for n in nodi:
            self._graph.add_node(self._idMapAP[n[0]])
        #print(*(n for n in self._graph.nodes()))



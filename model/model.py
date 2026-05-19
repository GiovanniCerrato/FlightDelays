import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._airports = DAO.getAllAirports()
        self._idMapAirports = {}
        for a in self._airports:
            self._idMapAirports[a.ID] = a

    def buildGraph(self,nMin):
        self._graph.clear()
        nodes = DAO.getAllNodes(nMin,self._idMapAirports)
        self._graph.add_nodes_from(nodes)

        # print(f"N nodi: {len(self._graph.nodes)}, n archi: {len(self._graph.edges)}")
        # self._addEdges()
        # print(f"N nodi: {len(self._graph.nodes)}, n archi:{len(self._graph.edges)}")
        # self._graph.clear_edges()
        self._addEdgesV2()
        print(f"N nodi: {len(self._graph.nodes)}, n archi:{len(self._graph.edges)}")

        print(*(n for n in self._graph.nodes()))

    def _addEdges(self):
        allTratte = DAO.getAllEdgesV1(self._idMapAirports)

        for t in allTratte:
            if t.aereoportoP in self._graph and t.aereoportoP in self._graph:
                #allora posso aggiungerlo
                if self._graph.has_edge(t.aereoportoP, t.aereoportoA):
                    self._graph[t.aereoportoP][t.aereoportoA]['weight'] += t.peso
                else:
                    self._graph.add_edge(t.aereoportoP, t.aereoportoA, weight=t.peso)

    def _addEdgesV2(self):
        allTratte = DAO.getAllEdgesV2(self._idMapAirports)
        for t in allTratte:
            if t.aereoportoP in self._graph and t.aereoportoA in self._graph:
                self._graph.add_edge(t.aereoportoP, t.aereoportoA, weight=t.peso)

    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getAllNodes(self):
        return self._graph.nodes




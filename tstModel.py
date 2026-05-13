from model.model import Model

m = Model()
m.buildGraph(5)
nNodes, nEdges = m.getGraphDetails()
print(f"Num nodes: {nNodes}, num edges:{nEdges}")
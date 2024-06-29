

class Node:
    def __init__(self, data):
        self.data = data
        self.edges = []

    def addEdge(self, edge):
        self.edges.append(edge)

    def __str__(self) -> str:
        return f"data: {self.data}"
    
    def __repr__(self) -> str:
        return f"data: {self.data}"

class Edge:
    def __init__(self, distance = 0, next_node = None) -> None:
        self.distance = distance
        self.next_node = next_node

def bfs_ll(node):
    set1 = set()
    queue = []
    list = []
    curr = node
    list.append(curr)
    set1.add(curr)
    while curr is not None:
        for edge in curr.edges:
            if edge.next_node not in set1:
                set1.add(edge.next_node)
                list.append(edge.next_node)
                queue.append(edge.next_node)
        try:
            curr = queue.pop(0)
        except:
            curr = None
    return list


def main():
    slc = Node("SLC")
    sea = Node("SEA")
    den = Node("DEN")
    port = Node("PORT")
    van = Node("VAN")
    van.addEdge(Edge(100, sea))
    sea.addEdge(Edge(100, van))
    slc.addEdge(Edge(700, sea))
    sea.addEdge(Edge(700, slc))
    sea.addEdge(Edge(200, port))
    port.addEdge(Edge(200, sea))
    slc.addEdge(Edge(200, den))

    res = bfs_ll(van)
    print(res)
    for node in res:
        print(node)
    

if __name__ == "__main__":
    main()
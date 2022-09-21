import collections

class DSNode:
    def __init__(self, x):
        self.parent = x
        self.rank = 0
    
class DisjointSet:
    """
    Disjoint set implementation with path compression. There are two optimizations here: the path compression and using rank to determine which subset to choose.
    Without any optimizations, you get potentially bad performance (i.e. calling union on two tall trees can take O(n)).
    
    With path compression, calling find(x) will always compress the height of the tree starting from x. 
    Adding rank comparisons with path compression (rank is the maximum height of a tree rooted at x) amortizes any operation on it to O(a(n)), 
    where a(n) is a near constant time.
    """
    def __init__(self, arr):
        self.nodes = {elem: DSNode(elem) for elem in arr}

    def union(self, a, b):
        """
        Union elements a and b. 
        """
        # find the parent elements
        a_parent = self.find(a)
        b_parent = self.find(b)

        if a_parent == b_parent: return

        # find the node references for each parent, and reassign parents based on rank
        a_node, b_node = self.nodes[a_parent], self.nodes[b_parent]
        if a_node.rank > b_node.rank:
            b_node.parent = a_parent
        elif a_node.rank < b_node.rank:
            a_node.parent = b_parent
        else:
            a_node.rank += 1
            b_node.parent = a_parent

    def find(self, elem):
        """
        Find and return the parent element within a set.
        """
        node = self.nodes[elem]
        if node.parent == elem: return elem
        node.parent = self.find(node.parent)
        return node.parent
     
    def __str__(self):
        sets = collections.defaultdict(set)
        for elem in self.nodes.keys():
            # could just call find, but this doesn't mutate the structure while printing
            curr = elem
            while curr != self.nodes[curr].parent:
                curr = self.nodes[curr].parent
            sets[curr].add(elem)
        return str([s for s in sets.values()])
            

if __name__ == "__main__":
    arr = ["a", "b", "c", "d", "e"]
    ds = DisjointSet(arr)
    ds.union("a", "b")
    ds.union("a", "c")
    ds.union("d", "e")
    ds.union("a", "e")
    print(ds)

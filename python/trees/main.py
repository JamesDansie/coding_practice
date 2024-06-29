def return_false():
    return False

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def traverse_print(node):
    if node is None:
        return
    traverse_print(node.left)
    print(node.data)
    traverse_print(node.right)

def traverse_max(node):
    if node is None:
        return float('-inf')
    return max(node.data, traverse_max(node.left), traverse_max(node.right))

def bfs_print(node):
    queue = []
    bfs_add_queue(node, queue)
    print("BFS traversal")
    while len(queue) > 0:
        print(queue.pop(0))

def bfs_add_queue(node, queue):
    if node is None:
        return
    queue.append(node.data)
    bfs_add_queue(node.left, queue)
    bfs_add_queue(node.right, queue)

def main():
    root = Node(1, left=Node(3), right=Node(10))
    root.left.left = Node(5)
    root.right.left = Node(7)
    root.right.right = Node(4)
    traverse_print(root)
    print(f"max is {traverse_max(root)}")
    bfs_print(root)

if __name__ == "__main__":
    main()
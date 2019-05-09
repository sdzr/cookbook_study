# 实现迭代协议
# 创建了一颗多叉树


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({})'.format(self._value)

    def __iter__(self):
        return iter(self._children)

    def add_children(self, node):
        self._children.append(node)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_children(child1)
    root.add_children(child2)
    child1.add_children(Node(3))
    child1.add_children(Node(4))
    child2.add_children(Node(5))

    for i in root.depth_first():
        print(i)

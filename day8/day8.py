import collections

Tree = collections.namedtuple('Tree', 'children, metadata')


def tree(numbers):
    num_children = numbers.popleft()
    num_metadata = numbers.popleft()
    return Tree(
        [tree(numbers) for _ in range(num_children)],
        [numbers.popleft() for _ in range(num_metadata)]
    )


def sum_metadata(tree):
    return sum(tree.metadata) + sum(map(sum_metadata, tree.children))


def node_value(tree):
    if not tree.children:
        return sum(tree.metadata)
    else:
        return sum(node_value(tree.children[key - 1]) for key in tree.metadata if key <= len(tree.children))


input = open("input.txt")

list = input.read().split(' ')

int_list = map(int, list)

numbers = collections.deque(int_list)

tree = tree(numbers)

print(sum_metadata(tree))
print(node_value(tree))
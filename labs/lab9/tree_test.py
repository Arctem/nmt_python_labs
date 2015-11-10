from tree import Tree

def main():
    tree = Tree('pie')
    tree.add_item('cake')
    tree.add_item('cookie')
    for item in tree:
        print('{}: {}'.format(item.datum, item.height()))
    #Should print:
    #cake: 0
    #pie: 1
    #cookie: 0

    tree.add_item('cupcake')
    for item in tree:
        print('{}: {}'.format(item.datum, item.height()))
    #Should print:
    #cupcake: 0
    #cake: 1
    #pie: 2
    #cookie: 0

    #this constructs the tree shown in the exercise
    other_tree = Tree(1)
    for i in [2, 3, 4, 6, 5, 7]:
        other_tree.add_item(i)
    print(list(map(lambda d: d.datum, other_tree)))
    #Should print: [4, 2, 5, 1, 6, 3, 7]


if __name__ == '__main__':
    main()

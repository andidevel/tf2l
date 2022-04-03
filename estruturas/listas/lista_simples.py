def add_item(name, root=None):
    if root is None:
        root = {
            'Name': name,
            'next': None
        }
        return root
    if root.get('next') is not None:
        add_item(name, root['next'])
        return None
    root['next'] = {
        'Name': name,
        'next': None
    }


def show_items(root):
    if root:
        print('[', end='')
        print(root['Name'], end='')
        next = root.get('next')
        while next is not None:
            print(f', {next["Name"]}', end='')
            next = next.get('next')
        print(']')


if __name__ == '__main__':
    print('Adicionando "A", "B", "C" à lista:')
    root = add_item('A', None)
    add_item('B', root)
    add_item('C', root)
    show_items(root)
    item = input('Novo item: ')
    add_item(item, root)
    show_items(root)
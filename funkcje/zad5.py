def DoAction(action, parameter):
    print("action:", action)
    print("parameter:", parameter)
    return


def DoAction2(action, *parameter):
    print('action:', action)
    print('parameter:', parameter)
    return

DoAction2('buy', 'shoes', 'socks', 'tshirt')


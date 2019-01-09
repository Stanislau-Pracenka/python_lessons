def func(*args):
    list_args = list(args)
    if len(args) == 0:
        print('Аргументы не указаны')
    if len(args) == 1:
        print(args)
    if len(args) > 1:
        slovar = {}
        for arg in args:
            if type(arg) not in slovar.keys():
                slovar[type(arg)] = 1
            else:
                slovar[type(arg)] += 1
        print(slovar)

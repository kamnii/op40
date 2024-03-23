# декораторы

def  function(func):
    def wrapp(*args, **kwargs):
        print('что-то сделал')
        res = func(*args, **kwargs)
        print('завершил результат')
        return res

    return wrapp


@function
def les(*args, **kwargs):
    print(f'адмирал {kwargs}')
    return f'вызов {args}'


# print(les("пяти", "адмиралов", маринфорд='акайну'))
les()

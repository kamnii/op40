# инкапсуляция +1
# 1 публичный 2 защищенный 3 скрытый
class Bank(object):
    name = 'Mbank'

    def __init__(self, name, key, balance=0):
        self.name = name
        self.__key = key
        self._balance = balance

    def Get_keys(self):
        self.__keys()

    def __keys(self):
        print(self.__key)

    def Set_keys(self, key):
        self.__key = key

    def __str__(self):
        return f'{self.name} {self._balance}'


kani = Bank('kani', '2525', 1000)
kani._balance = 100_000_000

kani.Get_keys()
kani.Set_keys(232323)
kani.Get_keys()

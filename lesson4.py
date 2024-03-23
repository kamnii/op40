# инкапсуляция +1
# 1 публичный 2 защищенный 3 скрытый
class Bank(object):
    name = 'Mbank'

    def __init__(self, name, key, balance=0):
        self.name = name
        self.__key = key
        self._balance = balance

    @property
    def get_key(self):
        return self.__key

    @get_key.setter
    def get_key(self, key):
        self.__key = key

    @get_key.deleter
    def get_key(self):
        del self.__key

    # def Get_keys(self):
    #     self.__keys()
    #
    # def __keys(self):
    #     print(self.__key)
    #
    # def Set_keys(self, key):
    #     self.__key = key

    def __str__(self):
        return f'{self.name} {self._balance}'


kani = Bank('kani', '2525', 1000)

print(kani.get_key)
kani.get_key = 1111111
print(kani.get_key)
del kani.get_key
# print(kani.get_key)
print(dir(kani))
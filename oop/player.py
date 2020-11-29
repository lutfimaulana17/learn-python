# class Player:
    # kalau sudah pakai self ga wajib di declair di awal
    # name  = ''
    # speed = ''

    # cuman sebagai tanda antar programmer bahwa variable nya privat contoh _age di program tetep sebagai variable biasa
    # private dari program __age pemanggilan bisa dari function tapi tidak bisa di akses langsung


    # def __init__(self, name, speed):
    #     self.name  = name
    #     self.speed = speed
    #     self.__age  = '23'


    # def getName(self, name):
    #     self.name = name
    #     return self.name

    # def getName(self):
    #     return self.name

    # def getSpeed(self):
    #     return self.speed

    # def getSkill(self):
    #     return 'normal'
    
    # def getAge(self):
    #     return self.__age


# pemain = Player()
# print(pemain.getName('Lutfi'))

# player = Player('Dybala', '86')
# player2 = Player('Messi', '90')
# print(player.getName() + " Punya Speed : " + player.getSpeed())
# print(player2.getName() + " Punya Speed : " + player2.getSpeed())


# class ArgentinaPlayer(Player):
#     def setAge(self, age):
#         self.age = age
#         return self.age

# class ArgentinaPlayer(Player):
#     def __init__(self, name, speed):
#         # Player.__init__(self, name, speed)
#         # cara lain pemanggilan init dari class parent 
#         super().__init__(name, speed)
#         print('Heeii argentina!')

#     def getSkill(self):
#         return 'cepat'

# class BrazilPlayer(Player):
#     def getSkill(self):
#         return 'samba'

# class BrazilPlayer(Player):
#     def getSkill(self):
#         return 'samba'


# playerArgen = ArgentinaPlayer('Lionel','67')
# print(playerArgen.getName() + ' Umurnya ' + playerArgen.setAge('24'))

# playerUser = ArgentinaPlayer('Lutfi', '22')
# playerUser.name = 'Maulana'
# age tidak bisa dirubah
# playerUser.__age = '89'
# print(playerUser.getAge() + ' namanya ' + playerUser.getName())

# class Player:

#     job = 'Pemain Bola'

#     def __init__(self, name):
#         self.name = name

#     def getName(self):
#         return self.name

# class method && static method bisa di pakai tanpa di declair terlebih dahulu
    # @staticmethod
    # def retiredIn(age):
    #     return str(40 - age)

    # class metod hanya bisa mengambil atau membaca static metod karna tidak behubungan dengan self
    # @classmethod
    # def generalInfo(cls, age):
    #     return cls.job + ' akan pensiun dalam ' + cls.retiredIn(age) +' tahun'


# player = Player('Lionel Messi')
# print(player.getName())
# print(Player.retiredIn(15))
# print(Player.generalInfo(5))

class Player:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    @property
    def infoPlayer(self):
        return self.name + ' adalah ' + self.age

    @infoPlayer.setter
    def infoPlayer(self, data):
        name, age = data.split(' ')
        self.name = name
        self.age  = age


player = Player('Lutfi', '22')
player.infoPlayer = 'Lutpy 22'
print(player.infoPlayer)


# nama = input("Siapa nama anda bos ?  ")
# umur = input("Umur mu piro bos ?  ")
# print("Salam kenal ya... " + nama + ". Kamu Sudah " + umur + " tahun")

# angka1 = 10
# angka2 = 20

# if angka1 == angka2:
#     print("iya anda benar angka 1 lebih kecil")
#     print("angka satunya adalah", angka1)
# else:
#     print("yah sayangnya anda salah")

# uang = input("Kamu uangnya berapa? ")
# utang = 10000

# if int(uang) < utang:
#     print("wah maaf bos ga cukup")
# elif int(uang) == utang:
#     print("terimakasih sudah bayar utangnya")    
# else:
#     print("wah uangnya lebih")

# and or pakai seperti ini & |

# syarat1 = True
# syarat2 = False

# if (4>2) & (8>7):
#     print('anda benar')
# else:
#     print('anda salah')

#looping while - for in

# count = 0

# while count < 5:
#     print('Yeay Yeay')
#     count = count + 1

# orang = ['lutfi', 'maulana', 'muhammad']

# for nama in orang:
#     print('nama namanya adalah', nama)

# text = 'python'

# for hurufnya in text:
#     print('ini huruf nya', hurufnya)

# loop pengulangan
# nested looping

# a = 1

# while a < 5:
#     b = 0
#     while b < a:
#         print("*", end='')
#         b = b + 1
#     print()
#     a = a + 1

# for a in range(1,5):
#     for b in range(1,5):
#         c = a * b
#         print(c, end="  ")
#     print()

# list

# orang = ['saputro', 'lutfi', 'maulana']
# umur = [10, 30, 20]
# mixed = [1, 'text', 'editor', 2.6]

# orang.append('indra')
# orang[2] = 'testing'
# del orang[1]

# print(orang)

# Tuples
# list yang immutable tidak dapat dirubah

# orang = ('saputro', 'lutfi', 'maulana')
# orang2 = ['saputro', 'lutfi', 'maulana']

# print(len(orang))
# mengubah dia menjadi list
# print(list(orang))
# merubah sebaliknya
# print(tuple(orang2))

# Dictionary

# data = {
#     'name': 'Lutfi',
#     'age': '22',
#     'hobby': 'Ngoding'
# }

# add/edit dictionary
# data['name'] = 'Maulana'
# data['dream'] = 'Programmer Remote'

# del data['age']

# print(data)

# for key, value in data.items():
#     print(key + " - " + value)

# Nested Dictionary

# data = {
#     1 : {
#         'name': 'Lutfi',
#         'age': '22',
#         'hobby': 'Ngoding'
#      },
#      2 : {
#         'name': 'Kanjuro',
#         'age': '22',
#         'hobby': 'Ngoding'
#      }
    
# }

# print(data[2]['name'])

# for key, value in data.items():
#     print("keynya ", key) 

#     for key2, value2 in value.items():
#         print(key2 + "-", value2)

# Sets data yang tidak bisa di akses dari key dan tidak ada yang kembar / tidak bisa kembar

# orang = {'lutfi', 'andi', 'vana', 'lutfi'}

# orang.add('fajar')
# orang.remove('andi')

# print(orang)

# angka1 = {1, 2, 3, 4, 5}
# angka2 = {4, 5, 6, 7, 8}

# print(angka1 | angka2)

# function

# def hitung(a, b):
#     print('Jumlah dari a dan b adalah', a + b)

# hitung(25, 78)

# def hitung(a, b):
#     c = a + b
#     return c

# print('textnya.. ', hitung(10, 20))

# func keyword argument

# def printData(name, hobby):
#     print('Namanya adalah ' + name + ' ' + 'Hobbynya adalah ' + hobby)

# printData(hobby = 'Ngoding', name = 'Lutfi')

# func *args: flexible jumlah send params ketika kita tidak tahu berapa params yang diterima

# def printData(*args):
#     for name in args:
#         print(name)
#     print(args)

# printData('Lutfi', 'Yudi', 'evana', 'fransisca')

# func *#Kwargs: flexible jumlah send params keywords argument

# def printData(**kwargs):
#     for key, value in kwargs.items():
#         print(value)
#     print(kwargs)

# printData(name = 'Lutfi', age = '22', hobby = 'menari')



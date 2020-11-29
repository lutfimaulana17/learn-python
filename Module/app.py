# import data as d
# from data import printNama

# print(d.person)

# printNama('jack')

# import datetime

# now = datetime.datetime.now()
# date = datetime.datetime(2020, 1, 1)
# now = datetime.datetime.now()

# print(now.strftime('%Y, %B, %d'))

# LOCAL DAN GLOBAL VARIABLE

# name = "Lutfi"

# edit variable global di function perlu tambahan global

# def printName():
#     global name
#     name = name + ' maulana'
#     print('akses dari dalam ' + name)

# printName()
# print('akses dari luar ' + name)

# Menghentikan code atau debuging

# raise Exception("stop ada kesalahan")

# try excepstion

# try:
#     print(nomor)
# except:
#     print('wow ada yang salah')

# assert

import sys

def is_it_linux():
    assert('linux' in sys.platform), "fungsi ini hanya untuk linux"

is_it_linux()
print('finish')
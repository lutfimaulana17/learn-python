# file = open('data.txt', 'r')
# file = open('data.txt', 'w')
# menambah data dengan tidak menghapus data lama
# file = open('data.txt', 'a+')
# file.write('\nOke Berhasil Ga Sih')

# file.seek(0)
# text = file.read()
# print(text)

file = open('data.txt', 'a+')

def add_to_list(newText):
    file.write('\n' + newText)
    ask_user()

def ask_user():
    namaItem = input('Mau Nulis Apa ?')
    add_to_list(namaItem)

ask_user()




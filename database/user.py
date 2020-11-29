from peewee import *

sqlite_db = SqliteDatabase('user.db')

class User(Model):
    name = CharField()
    email = CharField()

    class Meta:
        database = sqlite_db

sqlite_db.connect()
sqlite_db.create_tables([User])


# insert data
# User.create(name='lutfi', email='lutfi@binokular.net')

# alternatif
# user = User(name='lutfi2', email='lutfi2@binokular.net')
# user.save()

# user = User.insert(name='lutfi3', email='lutfi3@binokular.net').execute()

# hasilnya adalah idnya atau auto incnya
# print(user)

# insert many

# data_source = [
#     {'name': 'test1', 'email': 'test1@test.com'},
#     {'name': 'test2', 'email': 'test2@test.com'}
# ]

# User.insert_many(data_source).execute()

# alternatif insert many

# fields = [User.name, User.email]
# data = [
#     ('test3', 'test3@email.com'),
#     ('test4', 'test4@email.com')
# ]

# User.insert_many(data, fields=fields).execute()

# get data
# user1 = User.get(User.id == 4) 
# user1 = User.get(User.name == 'test) 
# cara simple

# user1 = User.get_by_id(4)

# user1 = User[4]


# print(user1.id)
# print(user1.name)
# print(user1.email)

# query = User.select()
# query = User.select().dicts()

# for user in query:
    # print(user.email)
    # print(user['email'])

# FILTERING
# user1 = User.select().where((User.name == 'test2') | (User.name == 'test3'))
# cara print
# for usr in user1:
#     print(usr.name)

# ini seperti query like
users = User.select().where(User.name.contains('test'))
for usr in users:
    print(usr.name)
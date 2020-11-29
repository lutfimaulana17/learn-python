import datetime
from peewee import *

db = SqliteDatabase('tweet.db')

class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)


class Tweet(BaseModel):
    user = ForeignKeyField(User, backref='tweets')
    message = TextField()
    create_date = DateTimeField(default=datetime.datetime.now)

# db.create_tables([User, Tweet])

# data = [
#     ('hilman', ('haloo tweet', 'ini tweet kedua saya', 'ini tweet ke tiga saya')),
#     ('lutfi', ('Heii Cantik', 'Kemana Saja Tak Ada Berita', 'Sedikit Cerita'))
# ]

# for username, tweets in data:
#     user = User.create(username = username)
#     for tweet in tweets:
#         Tweet.create(user=user, message=tweet)

# get data relation
query = Tweet.select().join(User).where(User.username == 'lutfi')
for tweet in query:
    print(tweet.message + " " + tweet.user.username)

# lutfiTweet = User.get(User.username == 'lutfi')
# for tweet in lutfiTweet.tweets:
#     print(tweet.message)

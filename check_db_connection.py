from fixture.db import DbFixture
import pymysql.cursors

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    users = db.get_user_list()
    for user in users:
        print(user)
    print(len(users))

finally:
    db.destroy()

#
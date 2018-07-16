from fixture.orm import ORMFixture
from model.Data import Group


check = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = check.get_users_in_group(Group(id='117'))
    for item in l:
        print(item)
    print(len(l))

finally:
    pass
    #db.destroy()

#
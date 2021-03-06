####
from model.Data import UsFo
import random


def test_delete_user(app, db, check_ui):
    if len(db.get_user_list()) == 0:
        app.user.Add_user(UsFo(firstname="test"))
    old_users = db.get_user_list()
    user = random.choice(old_users)
    app.user.delete_user_by_id(user.id)
    assert len(old_users) - 1 == app.user.counts()
    new_users = db.get_user_list()
    old_users.remove(user)
    assert old_users == new_users
    if check_ui:
        assert sorted(new_users, key=UsFo.id_or_max) == sorted(app.user.get_user_list(), key=UsFo.id_or_max)

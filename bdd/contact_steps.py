from pytest_bdd import given, when, then
from model.Data import UsFo
import random


@given('a user list')
def user_list(db):
    return db.get_user_list()


@given('a user with <firstname>, <lastname> and <company>')
def new_user(firstname, lastname, company):
    return UsFo(firstname=firstname, lastname=lastname, company=company)


@when('I add the user to the list')
def add_new_user(app, new_user):
    app.user.create(new_user)


@then('the new user list is equal to the old list with added user')
def verify_user_added(db, user_list, new_user):
    old_users = user_list
    new_users = db.get_user_list()
    old_users.append(new_user)
    assert sorted(old_users, key=UsFo.id_or_max) == sorted(new_users, key=UsFo.id_or_max)


@given('a non-empty user list')
def non_empty_user_list(db, app):
    if len(db.get_user_list()) == 0:
        app.user.create(UsFo(firstname="to delete"))
    return db.get_user_list()


@given('a random user from the list')
def random_user(non_empty_user_list):
    return random.choice(non_empty_user_list)


@when('I delete random user from the list')
def delete_user(app, random_user):
    app.user.delete_user_by_id(random_user.id)


@then('the new user list is equal to the old list without deleted user')
def verify_user_deleted(db, non_empty_user_list, random_user):
    old_users = non_empty_user_list
    new_users = db.get_user_list()
    assert len(old_users)-1 == len(new_users)
    old_users.remove(random_user)
    assert old_users == new_users
   # assert sorted(old_users, key=UsFo.id_or_max) == sorted(new_users, key=UsFo.id_or_max)


@given('a new user info with <firstname>, <lastname> and <company>')
def new_info(firstname, lastname, company):
    return UsFo(firstname=firstname, lastname=lastname, company=company)

@when('I modify random user from the list')
def modify_random_user(app, random_user, new_info):
    app.user.Edit_user_by_id(random_user.id, new_info)


@then('the new user list is equal to the old list without deleted user')
def verify_user_modify(db, non_empty_user_list, random_user, new_info):
    old_users = non_empty_user_list
    new_info.id == random_user.id
    old_users.remove(random_user)
    new_users = db.get_user_list()
    old_users.append(new_info)
    assert sorted(old_users, key=UsFo.id_or_max) == sorted(new_users, key=UsFo.id_or_max)
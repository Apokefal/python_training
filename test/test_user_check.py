import re
from random import randrange
from model.Data import UsFo


def test_user_check(app, db):
    if db.get_user_list() == 0:
        app.user.Add_user(UsFo(firstname="Walerko", lastname="Apokefal", address="Tomsk", homephone="123456789",
                               mobilephone="23456789", workphone="3456789", secondaryphone="45678901",
                               email="qwer@ty.com"))
    db_list = db.get_user_list()
    sorted_db_list = sorted(db_list, key=UsFo.id_or_max)
    ui_list = app.user.get_user_list()
    list_length = len(ui_list)
    sorted_ui_list = sorted(ui_list, key=UsFo.id_or_max)
    for index in range(0, list_length):
        assert sorted_ui_list[index].lastname == sorted_db_list[index].lastname
        assert sorted_ui_list[index].firstname == sorted_db_list[index].firstname
        assert sorted_ui_list[index].address == sorted_db_list[index].address
        assert sorted_ui_list[index].all_emails_from_home_page == merge_emails_like_on_home_page(sorted_db_list[index])
        assert sorted_ui_list[index].all_phones_from_home_page == merge_phones_like_on_home_page(sorted_db_list[index])


def clear_for_phones(s):
    return re.sub("[() -.]", "", s)

def merge_phones_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_for_phones(x),
                                filter(lambda x: x is not None,
                                        [user.homephone, user.mobilephone, user.workphone,
                                        user.secondaryphone]))))

def clear_for_emails(s):
    return re.sub("^\s*", "", s)

def merge_emails_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_for_emails(x),
                                filter(lambda x: x is not None,
                                       [user.email, user.email2, user.email3]))))

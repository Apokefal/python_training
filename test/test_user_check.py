import re
from random import randrange
from model.Data import UsFo


def test_user_check(app):
    if app.user.counts() == 0:
        app.user.Add_user(UsFo(firstname="Walerko", lastname="Apokefal", address="Tomsk", homephone="123456789",
                               mobilephone="23456789", workphone="3456789", secondaryphone="45678901",
                               email="qwer@ty.com"))
        all_users = app.user.get_user_list()
        index = randrange(len(all_users))
        user_from_home_page = app.user.get_user_list()[index]
        user_from_edit_page = app.user.get_user_info_from_edit_page(index)
        assert user_from_home_page.firstname == user_from_edit_page.firstname
        assert user_from_home_page.lastname == user_from_edit_page.lastname
        assert user_from_home_page.address == user_from_edit_page.address
        assert user_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(user_from_edit_page)
        assert user_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(user_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
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

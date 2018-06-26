

def test_phones_on_home_page(app):
    user_from_home_page = app.user.get_user_list()[0]
    user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    assert user_from_home_page.homephone == user_from_edit_page.homephone
    assert user_from_home_page.workphone == user_from_edit_page.workphone
    assert user_from_home_page.mobilephone == user_from_edit_page.mobilephone
    assert user_from_home_page.secondaryphone == user_from_edit_page.secondaryphone
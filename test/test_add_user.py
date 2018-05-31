# -*- coding: utf-8 -*-
import pytest
from model.Data import UsFo
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_test_add_user(app):
    app.session.Login(username="admin", password="secret")
    app.Add_user(UsFo(firstname="привет", middlename="привет", lastname="привет", nickname="привет", title="привет", company="привет", address="привет", home="привет", mobile="привет", work="привет", fax="привет", email="привет", email2="привет", email3="привет", homepage="привет", yearbirt="1989", yearanni="1989", address2="привет", phone2="привет", notes="привет"))
    app.session.Logout()


def test_test_add_empty_user(app):
    app.session.Login(username="admin", password="secret")
    app.Add_user(UsFo(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", yearbirt="", yearanni="", address2="", phone2="", notes=""))
    app.session.Logout()



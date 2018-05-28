# -*- coding: utf-8 -*-
import pytest
from userform import UsFo
from contr import Contr

@pytest.fixture()
def ctr(request):
    fixture = Contr()
    request.addfinalizer(fixture.murder)
    return fixture

def test_test_add_user(ctr):
    ctr.Login(username="admin", password="secret")
    ctr.Add_user(UsFo(firstname="привет", middlename="привет", lastname="привет", nickname="привет", title="привет", company="привет", address="привет", home="привет", mobile="привет", work="привет", fax="привет", email="привет", email2="привет", email3="привет", homepage="привет", yearbirt="1989", yearanni="1989", address2="привет", phone2="привет", notes="привет"))
    ctr.Logout()

def test_test_add_empty_user(ctr):
    ctr.Login(username="admin", password="secret")
    ctr.Add_user(UsFo(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", yearbirt="", yearanni="", address2="", phone2="", notes=""))
    ctr.Logout()

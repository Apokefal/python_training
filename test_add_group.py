# -*- coding: utf-8 -*-
import pytest
from Data import Group
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_group(app):
    app.Login(username="admin", password="secret")
    app.create_group(Group(name="apo", header="apok", footer="apokefa"))
    app.Logout()


def test_test_add_empty_group(app):
    app.Login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.Logout()

def test_test_add_incorrect_group(app):
    app.Login(username="admin", password="secret")
    app.create_group(Group(name="%", header="%", footer="%"))
    app.Logout()

# -*- coding: utf-8 -*-
import pytest
from model.Data import Group
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_group(app):
    app.session.Login(username="admin", password="secret")
    app.create_group(Group(name="apo", header="apok", footer="apokefa"))
    app.session.Logout()


def test_test_add_empty_group(app):
    app.session.Login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.Logout()

def test_test_add_incorrect_group(app):
    app.session.Login(username="admin", password="secret")
    app.create_group(Group(name="%", header="%", footer="%"))
    app.session.Logout()

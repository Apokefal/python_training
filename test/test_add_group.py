# -*- coding: utf-8 -*-
from model.Data import Group


def test_test_add_group(app):
    app.session.Login(username="admin", password="secret")
    app.group.create(Group(name="apo", header="apok", footer="apokefa"))
    app.session.Logout()


def test_test_add_empty_group(app):
    app.session.Login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.Logout()

def test_test_add_incorrect_group(app):
    app.session.Login(username="admin", password="secret")
    app.group.create(Group(name="%", header="%", footer="%"))
    app.session.Logout()

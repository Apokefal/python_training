# -*- coding: utf-8 -*-
from model.Data import Group


def test_test_add_group(app):
    app.group.create(Group(name="apo", header="apok", footer="apokefa"))

def test_test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

def test_test_add_incorrect_group(app):
    app.group.create(Group(name="%", header="%", footer="%"))


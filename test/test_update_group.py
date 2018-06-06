from model.Data import Group

def test_update_group_name(app):
    app.group.Edit_first_group(Group(name="New group"))

def test_update_group_header(app):
    app.group.Edit_first_group(Group(header="New header"))

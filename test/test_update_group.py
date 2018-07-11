###
from model.Data import Group
import random

def test_update_group_name(app, db, check_ui):
    group = Group(name="Newgroup1", header="Newheader2", footer="Newfooter3")
    if len(db.get_group_list()) == 0:
        app.group.create(group)
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)
    #index = randrange(len(old_groups))
    #group.id = old_groups[index].id
    app.group.Edit_group_by_id(random_group.id, group)
    new_groups = db.get_group_list()
    group.id = random_group.id
    old_groups.remove(random_group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_update_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="Test"))
#    old_groups = app.group.get_group_list()
#    app.group.Edit_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)

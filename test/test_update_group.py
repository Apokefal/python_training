###
from model.Data import Group
import random

def test_update_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    #index = randrange(len(old_groups))
    group_data = Group(name="Newgroup1", header="Newheader2", footer="Newfooter3")
    #group.id = old_groups[index].id
    app.group.Edit_group_by_id(group.id, group_data)
    new_groups = db.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups.append(group_data)
    old_groups.remove(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_update_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="Test"))
#    old_groups = app.group.get_group_list()
#    app.group.Edit_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)

from model.Data import UsFo


def test_delete_user(app):
    if app.user.counts() == 0:
        app.user.Add_user(UsFo(firstname="test"))
    app.user.delete_first_user()

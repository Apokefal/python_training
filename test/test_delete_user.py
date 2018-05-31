def test_delete_user(app):
    app.session.Login(username="admin", password="secret")
    app.user.delete_fisrt_user()
    app.session.Logout()
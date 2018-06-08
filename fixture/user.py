class UserHelper:
    def __init__(self, app):
        self.app = app

    def Open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")

    def Add_user(self, user):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_user_form(user)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.Return_home_page()

    def fill_user_form(self, user):
        wd = self.app.wd
        self.change_field_value("firstname", user.firstname)
        self.change_field_value("middlename", user.middlename)
        self.change_field_value("lastname", user.lastname)
        self.change_field_value("nickname", user.nickname)
        self.change_field_value("title", user.title)
        self.change_field_value("company", user.company)
        self.change_field_value("address", user.address)
        self.change_field_value("home", user.home)
        self.change_field_value("mobile", user.mobile)
        self.change_field_value("work", user.work)
        self.change_field_value("fax", user.fax)
        self.change_field_value("email", user.email)
        self.change_field_value("email2", user.email2)
        self.change_field_value("email3", user.email3)
        self.change_field_value("homepage", user.homepage)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[4]").click()
        self.change_field_value("byear", user.yearbirt)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[4]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[5]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[5]").click()
        self.change_field_value("ayear", user.yearanni)
        self.change_field_value("address2", user.address2)
        self.change_field_value("phone2", user.phone2)
        self.change_field_value("notes", user.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def Edit_user(self, new_user_data):
        wd = self.app.wd
        self.select_first()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_user_form(new_user_data)
        # Submit group creation
        wd.find_element_by_name("update").click()

    def select_first(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_user(self):
        wd = self.app.wd
        self.select_first()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.Open_home_page()

    def Return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def counts(self):
        wd = self.app.wd
        self.Open_home_page()
        return len(wd.find_elements_by_name("selected[]"))



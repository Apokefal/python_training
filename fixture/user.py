#####
from model.Data import UsFo
import re

class UserHelper:
    def __init__(self, app):
        self.app = app

    def Open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") and len(wd.find_elements_by_name("searchform")) > 0):
            wd.get("http://localhost/addressbook/")

    def Add_user(self, user):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_user_form(user)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.Return_home_page()
        self.user_cache = None

    def fill_user_form(self, user):
        wd = self.app.wd
        self.change_field_value("firstname", user.firstname)
        self.change_field_value("lastname", user.lastname)
        self.change_field_value("address", user.address)
        self.change_field_value("home", user.homephone)
        self.change_field_value("mobile", user.mobilephone)
        self.change_field_value("work", user.workphone)
        self.change_field_value("phone2", user.secondaryphone)
        self.change_field_value("email", user.email)
        self.change_field_value("email2", user.email2)
        self.change_field_value("email3", user.email3)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first(self):
        self.select_user_by_index()

    def select_user_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_user_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def Edit_user(self):
        self.Edit_user_by_index(0)

    def Edit_user_by_index(self, index, new_user_data):
        wd = self.app.wd
        self.select_user_by_index(index)
        wd.find_elements_by_xpath("//a[contains(@href,'edit.php?id=')]")[index].click()
        self.fill_user_form(new_user_data)
        # Submit group creation
        wd.find_element_by_name("update").click()
        self.user_cache = None

    def Edit_user_by_id(self, id, new_user_data):
        wd = self.app.wd
        self.select_user_by_id(id)
        wd.find_element_by_xpath("//a[contains(@href, %s) and contains(@href, 'edit.php?id=')]" % id).click()
        self.fill_user_form(new_user_data)
        # Submit group creation
        wd.find_element_by_name("update").click()
        self.user_cache = None

    def delete_first_user(self):
        self.delete_user_by_index(0)

    def delete_user_by_index(self, index):
        wd = self.app.wd
        self.select_user_by_index(index)
        wd.find_element_by_css_selector("input[value=Delete]").click()
        wd.switch_to_alert().accept()
        self.Open_home_page()
        self.user_cache = None

    def delete_user_by_id(self, id):
        wd = self.app.wd
        self.select_user_by_id(id)
        wd.find_element_by_css_selector("input[value=Delete]").click()
        wd.switch_to_alert().accept()
        self.Open_home_page()
        self.user_cache = None

    def Return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def counts(self):
        wd = self.app.wd
        self.Open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    user_cache = None

    def get_user_list(self):
        if self.user_cache is None:
            wd = self.app.wd
            self.Open_home_page()
            self.user_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.user_cache.append(UsFo(firstname=firstname, lastname=lastname, id=id, address=address,
                                            all_emails_from_home_page=all_emails,
                                            all_phones_from_home_page=all_phones))
        return list(self.user_cache)

    def open_user_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.Open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_user_view_by_index(self, index):
        wd = self.app.wd
        self.app.Open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_user_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_user_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return UsFo(firstname=firstname, lastname=lastname, id=id, address=address,
                    homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                    secondaryphone=secondaryphone, email=email, email2=email2, email3=email3)

    def get_user_from_view_page(self, index):
        wd = self.app.wd
        self.open_user_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return UsFo(homephone=homephone, mobilephone=mobilephone,
                    workphone=workphone, secondaryphone=secondaryphone)
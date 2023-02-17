from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.driver
        wd.find_element(By.LINK_TEXT, "groups").click()

    def change_field_value(self, field_name, text):
        wd = self.app.driver
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def create(self, group):
        wd = self.app.driver
        self.open_group_page()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_group_page()

    def select_first_group(self):
        wd = self.app.driver
        wd.find_element(By.NAME, "selected[]").click()

    def delete_first_group(self):
        wd = self.app.driver
        self.open_group_page()
        self.select_first_group()
        # submit group deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_group_page()

    def modify_first_group(self, new_group_date):
        wd = self.app.driver
        self.open_group_page()
        self.select_first_group()
        # open modification form
        wd.find_element(By.NAME, "edit").click()
        # fill group form
        self.fill_group_form(new_group_date)
        # submit modification
        wd.find_element(By.NAME, "update").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        wd = self.app.driver
        wd.find_element(By.LINK_TEXT, "group page").click()

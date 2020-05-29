import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class PythonTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="geckodriver.exe")

    def test_signup(self):
        self.signup("selenium@selenium.com", "selenium", "selenium")
        time.sleep(1)
        self.assertIn("Login", self.driver.title)

        self.login("selenium", "selenium")
        time.sleep(1)
        self.assertIn("blog_website", self.driver.title)

    def test_login(self):
        self.login("selenium", "selenium")
        time.sleep(1)
        self.assertIn("blog_website", self.driver.title)

    def test_logout(self):
        self.login("selenium", "selenium")
        time.sleep(1)
        self.assertIn("blog_website", self.driver.title)

        logout_link = self.driver.find_element_by_partial_link_text("Logout")
        logout_link.click()
        time.sleep(1)
        self.assertIn("!NVITE", self.driver.title)

    def test_create_blog(self):
        self.create_blog("Blog by Selenium", "Selenium for system testing")
        self.assertIn("selenium", self.driver.current_url)

        my_blog_link = self.driver.find_element_by_link_text("My Blogs")
        my_blog_link.click()
        self.assertIn("/myblog", self.driver.current_url)

        created_blog_title = self.driver.find_elements_by_tag_name("h2")[-1].text
        self.assertEqual("Blog by Selenium", created_blog_title)

    def test_view_blog(self):
        self.view_blog()
        time.sleep(1)
        self.assertIn("/allblogs/", self.driver.current_url)

    def test_like_blog(self):
        prev_likes = self.view_blog()
        time.sleep(1)
        self.assertIn("/allblogs/", self.driver.current_url)

        like_btn = self.driver.find_element_by_name("submit")
        like_btn.click()

        self.driver.back()
        self.driver.back()
        self.driver.refresh()

        likes_field = self.driver.find_element_by_class_name("badge")
        curr_likes = int(likes_field.text[7:])
        self.assertEqual(prev_likes, curr_likes-1)

    def test_view_comments(self):
        self.view_comments()
        time.sleep(1)
        self.assertIn("/comments", self.driver.current_url)

    def test_add_comment(self):
        self.add_comment("Comment by selenium")
        time.sleep(1)
        comments = self.driver.find_elements_by_tag_name("p")
        self.assertEqual("Comment by selenium", comments[-4].text)

    def test_spam_detection(self):
        self.create_blog("Winner", "You have won a lottery")
        self.assertIn("selenium", self.driver.current_url)

        explore_link = self.driver.find_element_by_link_text("Explore")
        explore_link.click()
        self.assertIn("/allblogs", self.driver.current_url)

        created_blog_link = self.driver.find_elements_by_class_name("list-group-item")[-1]
        self.assertIn("SPAM", created_blog_link.text)

    def login(self, username, password):
        self.driver.get("http://127.0.0.1:8000")
        login_btn = self.driver.find_element_by_link_text("Login")
        login_btn.click()

        self.assertIn("Login", self.driver.title)

        username_field = self.driver.find_element_by_name("username")
        username_field.send_keys(username)

        pass_field = self.driver.find_element_by_name("pass")
        pass_field.send_keys(password)
        pass_field.send_keys(Keys.RETURN)

    def signup(self, email, username, password):
        self.driver.get("http://127.0.0.1:8000")
        signup_btn = self.driver.find_element_by_link_text("Signup")
        signup_btn.click()

        self.assertIn("login_page", self.driver.title)

        email_field = self.driver.find_element_by_name("email")
        email_field.send_keys(email)

        name_field = self.driver.find_element_by_name("name")
        name_field.send_keys(username)

        pass_field = self.driver.find_element_by_name("pwd")
        pass_field.send_keys(password)
        pass_field.send_keys(Keys.RETURN)

    def create_blog(self, title, content):
        self.login("selenium", "selenium")
        time.sleep(1)
        self.assertIn("blog_website", self.driver.title)

        create_blog_link = self.driver.find_element_by_link_text("Create blog")
        create_blog_link.click()
        self.assertIn("/createblog", self.driver.current_url)

        blog_title_field = self.driver.find_element_by_name("title")
        blog_title_field.send_keys(title)

        content_field = self.driver.find_element_by_name("textarea1")
        content_field.send_keys(content)

        add_btn = self.driver.find_element_by_id("submit1")
        add_btn.click()

    def view_blog(self):
        self.login("selenium", "selenium")
        time.sleep(1)
        self.assertIn("blog_website", self.driver.title)

        explore_link = self.driver.find_element_by_link_text("Explore")
        explore_link.click()
        self.assertIn("/allblogs", self.driver.current_url)

        likes_field = self.driver.find_element_by_class_name("badge")
        likes = int(likes_field.text[7:])

        blog_link = self.driver.find_element_by_class_name("list-group-item")
        blog_link.click()
        return likes

    def view_comments(self):
        self.view_blog()
        time.sleep(1)
        self.assertIn("/allblogs/", self.driver.current_url)

        comments_btn = self.driver.find_element_by_link_text("Comment")
        comments_btn.click()

    def add_comment(self, comment):
        self.view_comments()
        time.sleep(1)
        self.assertIn("/comments", self.driver.current_url)

        comment_box = self.driver.find_element_by_id("area")
        comment_box.send_keys(comment)
        comment_box.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)

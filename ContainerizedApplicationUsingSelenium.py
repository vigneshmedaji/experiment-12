import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class ContainerAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://localhost:8080")

    def test_page_title(self):
        self.assertEqual(
            self.driver.title,
            "Docker Application"
        )

    def test_heading(self):
        heading = self.driver.find_element(
            By.TAG_NAME, "h1"
        )
        self.assertEqual(
            heading.text,
            "Hello from Docker!"
        )

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

from django.test import TestCase
from django.test import Client
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By


class WebTest(TestCase):
    """
    Tests that are related to the templates and views and urls.
    """

    root_url = "http://127.0.0.1:8000"

    def setUp(self):
        self.client = Client()
        self.selenium = Firefox()

    def test_index_url_200(self):
        """
        Tests if the index url is working.
        """

        response = self.client.get("")
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        """
        Tests if the index template renders correctly.
        """

        self.selenium.get(self.root_url)
        element = self.selenium.find_elements(By.TAG_NAME, "body")
        self.assertGreater(len(element), 0)

    def tearDown(self):
        del self.client
        self.selenium.close()

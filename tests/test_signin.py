import pytest

from main import get_html_content, get_content_from_container, initialize_driver

class TestSample:

    def __init__(self):
        self.driver = initialize_driver()

    def test_render_signin_screen_success(self):
        soup = get_html_content(self.driver, "https://focusearth.dev-16.toolbox.am/login")
        res = get_content_from_container(soup, "h2")
        title = "Welcome to the Energy Portal"
        assert title == res[-1].text

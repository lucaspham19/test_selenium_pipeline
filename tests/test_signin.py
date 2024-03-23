import pytest

from main import get_html_content

class TestSample:

    def test_render_signin_screen_success(self):
        content = get_html_content("https://focusearth.dev-16.toolbox.am/login")
        # title = "Google"
        # assert title == driver.title

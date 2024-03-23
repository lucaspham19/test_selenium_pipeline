import pytest

@pytest.mark.usefixtures('driver')
class TestSample:

    def test_render_signin_screen_success(self, driver):
        driver.get('https://google.com/ncr')
        title = "Google"
        assert title == driver.title

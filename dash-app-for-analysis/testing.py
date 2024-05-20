from Pink_morsel_DashAppCode import app
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()



def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=10)


def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#radio-items", timeout=10)


def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#pink-morsel-graph", timeout=10)
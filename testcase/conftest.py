from pageobject.login import Login
from pageobject.setting import Setting
from pageobject.api_login import Login as RLogin
import pytest

lg = Login()
st = Setting()
rg = RLogin()

@pytest.fixture(scope="function")
def init_fun(driver):
    lg.login(driver, 'lilinlinmail@163.com', 'linlin55')
    yield driver
    st.dele_sign(driver)


@pytest.fixture(scope="function")
def login_renren():
    rg.login('15900715134', '73cace3274ebcd9b223640c3c5977cd8a019d1a04e10f3825dd55ba1643ff366')
    yield

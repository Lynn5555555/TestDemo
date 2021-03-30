from pageobject.api_login import Login
from pageobject.api_ziliao import Ziliao
from common.read_yaml import readyml
import pytest
import os
import allure

root_path = os.path.dirname(os.path.dirname(__file__))
yaml_path = os.path.join(root_path, 'data', 'caseData.yaml')

lg = Login()
zl = Ziliao()
yaml_info = readyml(yaml_path)['TestCase']


class TestRen():

    @allure.feature("登录")
    @pytest.mark.parametrize('yaml_info', yaml_info['case1'])
    def test_renren_01(self,yaml_info):
        '''人人网正常登录'''
        with allure.step("开始登录"):
            res = lg.login(yaml_info['username'], yaml_info['psw'])
            assert res['code'] == True

    @pytest.mark.parametrize('yaml_info', yaml_info['case2'])
    @pytest.mark.usefixtures("login_renren")
    def test_renren_02(self,yaml_info):
        '''人人网编辑爱好'''
        res = zl.edit_hobby(yaml_info['music'],yaml_info['interest'],yaml_info['book'],yaml_info['movie'],yaml_info['game'],yaml_info['comic'],yaml_info['sport'])
        assert res == True

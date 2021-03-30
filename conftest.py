#!/usr/bin/python
# -*- coding:utf-8 -*-

import pytest
from py._xmlgen import html
from selenium import webdriver
from PIL import ImageGrab
from io import BytesIO
import base64, os
from common.guibase import GuiBase
from common.globalmanager import GlobalManager
from common.config import Config

from pageobject.login import Login
from pageobject.setting import Setting

lg = Login()
st = Setting()
config = Config.getConfig()
rootPath = GlobalManager.globaldict['rootPath']
_driver = None

def pytest_addoption(parser):
    '''添加命令行参数--browser、--host'''
    parser.addoption(
        "--browser", action="store", default=config['browser']['type'], help="browser option: firefox or chrome"
             )
    # 添加host参数，设置默认测试环境地址
    parser.addoption(
        "--host", action="store", default=config['url']['sic'], help="test host->http://10.11.1.171:8888"
    )

"""
Summary部分在此设置
"""


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix, summary, postfix):
    # Get configure content.
    prefix.extend([html.p("测试开发组: 李林琳")])




"""
Results部分在此设置.
"""


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.pop(-1)
    cells.insert(1, html.th('Description'))
    # cells.insert(3, html.th('Time', class_='sortable time', col='time'))
    # cells.insert(1,html.th("Test_nodeid"))


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.pop(-1)
    cells.insert(1, html.td(report.description))
    # cells.insert(3, html.td(datetime.utcnow(), class_='col-time'))
    # cells.insert(1,html.td(report.nodeid))


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")  # 设置编码显示中文


@pytest.fixture(scope='session')
def driver(request):
    '''定义全局driver参数'''
    global _driver
    if _driver is None:
        name = request.config.getoption("--browser")
        if name == "firefox":
            _driver = webdriver.Firefox(executable_path=os.path.join(rootPath, config['browser']['exec_path'], "gecokdriver.exe"))
        elif name == "chrome":
            _driver = webdriver.Chrome(executable_path=os.path.join(rootPath, config['browser']['exec_path'], "chromedriver.exe"))
        else:
            _driver = webdriver.Ie(executable_path=os.path.join(rootPath, config['browser']['exec_path'], "IEDriverServer.exe"))
        print("正在启动浏览器名称：%s" % name)

    def fn():
        print("当全部用例执行完之后：teardown quit driver！")
        _driver.quit()
    request.addfinalizer(fn)
    return _driver


@pytest.fixture(scope='session')
def host(request):
    '''全局host参数'''
    return request.config.getoption("--host")

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """当测试失败的时候，自动截图，展示到html报告中"""
    outcome = yield
    pytest_html = item.config.pluginmanager.getplugin('html')

    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):  # 失败截图
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="lookimg(this.src)" align="right"/></div>' % screen_img
                js_html = '''
                <script>
                    function lookimg(str)
                    {
                        var newwin=window.open();
                        newwin.document.write("<img src="+str+" />");
                    }
                </script>
                '''#######js不会以后再搞
                extra.append(pytest_html.extras.html(html))
                extra.append(pytest_html.extras.html(js_html))
        report.extra = extra
        report.description = str(item.function.__doc__)


def _capture_screenshot():
    output_buffer = BytesIO()
    img = ImageGrab.grab()
    img.save(output_buffer, "png")
    bytes_value = output_buffer.getvalue()
    return base64.b64encode(bytes_value).decode()


@pytest.fixture(scope="session", autouse=True)
def screen_size_check():
    print("check screen resolution")
    GuiBase.screen_size_check()





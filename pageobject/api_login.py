from common.apibase import ApiBase

api = ApiBase()


class Login():

    def login(self, username, psw):
        '''人人网登录'''
        url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2021201920756"

        header = {
            "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "email": username,
            "icode": "",
            "origURL": "http://www.renren.com/home",
            "domain": "renren.com",
            "key_id": "1",
            "captcha_type": "web_login",
            "password": psw,
            "rkey": "08dfc31399cf0baa6abdfeb324016e2b",
            "f": "http%3A%2F%2Fwww.renren.com%2FLogout.do%3Frequesttoken%3D-349286761"
        }

        res = api.post(url, data, headers=header)
        return res.json()


if __name__ == '__main__':
    lg = Login()
    a = lg.login('15900715134', '73cace3274ebcd9b223640c3c5977cd8a019d1a04e10f3825dd55ba1643ff366')
    print(a)

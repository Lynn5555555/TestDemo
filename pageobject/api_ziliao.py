from common.apibase import ApiBase

api = ApiBase()


class Ziliao():

    def edit_hobby(self, music, interest, book, movie, game, comic, sport):
        '''编辑爱好'''

        url = 'http://www.renren.com/PersonalInfo.do?v=info_timeline'
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "music": music,
            "interest": interest,
            "book": book,
            "movie": movie,
            "game": game,
            "comic": comic,
            "sport": sport,
            "errorReturn": "1",
            "submit": "保存",
            "requestToken": "39957779",
            "_rtk": "ce22b36d"
        }
        res = api.post(url, data, headers=header)
        if res.status_code == 200:
            return True
        else:
            return False


if __name__ == '__main__':
    from pageobject.api_login import Login
    lg = Login()
    lg.login('15900715134', '73cace3274ebcd9b223640c3c5977cd8a019d1a04e10f3825dd55ba1643ff366')
    zl = Ziliao()
    a = zl.edit_hobby('这是音乐111', '这是爱好111', '这是书籍111', '这是电影111', '这是游戏111', '这是动漫111', '这是运动111')
    print(a)

import requests

class UnsplashSource:

    host = 'https://source.unsplash.com'
    random_url = host + '/random'
    user_url = host + '/user/'
    user_like_url = user_url + '/likes'

    def __enter__(self):
        self.session = requests.Session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self.session.close()

    def random(self, size=800):
        """获取随机图片"""
        print("随机图片")
        resp = self.session.get(self.random_url + f'/{size}x0')
        print("获取图片。。。")
        return resp.content

    def keywords(self, keys, size=800):
        keys = keys.replace(' ', ',')
        resp = self.session.get(self.random_url + f'/{size}x0/?{keys}')
        return resp.content

    def keywords_url(self, keys, size=400):
        keys = keys.replace(' ', ',')
        with requests.Session() as s:
            resp = s.get(self.random_url + f'/{size}x0/?{keys}', allow_redirects=False)
            return resp.headers['location']



if __name__ == '__main__':
    # with UnsplashSource() as client:
    #     picture = client.random(400)
    #     with open('demo.jpg', 'wb') as f:
    #         f.write(picture)
    # import io
    # from PIL import Image
    #
    #
    # with UnsplashSource() as client:
    #
    #     picture = client.keywords('girl', size=400)
    #     print("完成下载")
    #     # 读取完整
    #     im = Image.open(io.BytesIO(picture))
    #     # # 按尺寸读取
    #     # im = Image.frombuffer('RGB', (400, 300), picture)
    #     a = im.show()
    #     print("show", a)

    with UnsplashSource() as c:
        resp = c.keywords_url('girls', size=400)
        print(resp)
import requests


def get_photos(order_by='popular', page=1, per_page=50):
    """通过developer api 获取图片地址。"""
    session = requests.Session()
    url = 'https://api.unsplash.com/photos'
    params = {
        "client_id": "u-eIuJk1zmvplc2EeZK5NGIMBvsEJJj6PfGlM4ockOE",
        "order_by": order_by,
        "page": page,
        "per_page": per_page
    }
    resp = session.get(url, params=params).json()
    return resp


def search_photos(keyword, order_by='relevant', page=1, per_page=50):
    """通过关键字搜索获取图片。"""
    session = requests.Session()
    url = 'https://api.unsplash.com/search/photos'
    params = {
        "client_id": "u-eIuJk1zmvplc2EeZK5NGIMBvsEJJj6PfGlM4ockOE",
        "query": keyword,
        "page": page,
        "order_by": order_by,
        "per_page": per_page
    }
    resp = session.get(url, params=params).json()
    return resp


if __name__ == '__main__':
    pass

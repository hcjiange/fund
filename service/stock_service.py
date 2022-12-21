import requests
import json

# 获取股票 - 和讯
def get_stocks(block: int = 252, rows: int = 500, start: int = 0):
    url = "http://webstock.quote.hermes.hexun.com/a/sortlist"
    params = {
        "block": block,
        "commodityid": 0,
        "title": 15,
        "direction": 0,
        "start": start,
        "number": rows,
        "input": "undefined",
        "column": "code,name,price,updownrate,LastClose,open,high,low,volume,priceweight,amount,exchangeratio,VibrationRatio,VolumeRatio"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
        "Referer": "http: //quote.hexun.com/"
    }
    req = requests.get(url=url, params=params, headers=headers)
    req.content.decode("utf-8")
    response = req.text
    req.close()
    res = json.loads(response[1:-2])
    data = []
    if "Data" in res.keys():
        for data_list in res['Data']:
            for item in data_list:
                data.append(item)

    return data


# 雪球股票
def get_list(page: int = 1, size: int = 1000, type: str = "sh_sz", order_by: str = "current_year_percent"):
    params = {
        'page': page,
        'size': size,
        'order': "desc",
        'orderby': order_by,
        'order_by': order_by,
        'market': "CN",
        'type': type,
    }
    headers = {
        # ':authority': 'stock.xueqiu.com',
        'cookie': "device_id=2fd33de446466b8053638f07d480b33f; s=bk1admfkds; Hm_lvt_1db88642e346389874251b5a1eded6e3=1668560831; xq_a_token=df4b782b118f7f9cabab6989b39a24cb04685f95; xqat=df4b782b118f7f9cabab6989b39a24cb04685f95; xq_r_token=3ae1ada2a33de0f698daa53fb4e1b61edf335952; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY3MjE4Njc1MSwiY3RtIjoxNjY5ODY2NTUxMjg3LCJjaWQiOiJkOWQwbjRBWnVwIn0.G2XnhWphDn819jXeG5BP38lN4BTfbYp45eUML-vNzmk-kQ8i0B5hbq8O7x_aYAXKJ9whAOzV48bqwX4-qUzXA1iYcsEtJhJc8A0Cn_rG1b4GWxyIM01x3DXNRlLdxMH4HNc52op_rpnfrb7tQ9ybWz8lTC9z-odN-RsG2vlH99GGCWM24OvB78ktP17XFqz53dzwE1mEGoTE7bBDyzndEnGuCCoODiPONSZLUi33XL9c2DrUV4UNBT2kYoQNfImpEp1LjdjMtrZ7omRH8X-VHhBFb4mkTnmQj4jjg6NsOFfdfH6Dm2G-6qLP_DlDoxMN2hk0LjNbx7v0j8_vWh9ysQ; u=541669866561641; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1670337296",
        'origin': "https://xueqiu.com",
        'referer': "https://xueqiu.com/hq",
        'se-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': "?0",
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': "empty",
        'sec-fetch-mode': "cors",
        'sec-fetch-site': "same-site",
        'user-agent': "Mozi"
    }
    url = "https://stock.xueqiu.com/v5/stock/screener/quote/list.json"

    req = requests.get(url=url, params=params, headers=headers)
    req.content.decode("utf-8")
    response = req.text
    return response
    req.close()
    res = json.loads(response)
    data = []
    if "data" in res.keys():
        if "list" in res['data'].keys():
            data = res['data']['list']
    return data
# 雪球网的数据格式是json字符串
#
# https://xueqiu.com/stock/forchartk/stocklist.json?symbol=代码&period=1day&type=复权还是不复权&begin=开始时间时间戳&end=结束时间时间戳&_=结束时间时间戳
#
# 地址参数：上海股票在编号前加SH，深圳股票，在编号前加SZ，period代表的时间间隔，复权不复权使用after和before表示，开始时间和结束时间要用时间戳表示。
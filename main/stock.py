from service import stock_service
from model import stock_model
import time


def sync_stocks():
    # 每次数量
    page_size = 1
    # 开始页
    page = 1
    # 数据类型
    type = "sh_sz"
    while True:
        stocks = stock_service.get_list(page, page_size, type)
        print(stocks)
        return
        if not len(stocks) > 0:
            break

        new_stocks = []
        for stock in stocks:
            new_stocks.append({
                'code': stock[0],
                'name': stock[1],
                'block': block,
                'price': stock[2] * 0.01,
                'updown_rate': stock[3] * 0.01,
                'last_close': stock[4] * 0.01,
                'open': stock[5] * 0.01,
                'high': stock[6] * 0.01,
                'low': stock[7] * 0.01,
                'volume': stock[8] * 0.01,
                'amount': stock[10] * 0.01,
                'exchange_ratio': stock[11] * 0.01,
                'vibration_ratio': stock[12] * 0.01,
                'volume_ratio': stock[13] * 0.01
            })
        stock_obj = stock_model.StockModel()
        res = stock_obj.add_all(new_stocks)
        print(res)
        time.sleep(1)
        page += 1


def sync_net_data():
    stock_service.get_data()

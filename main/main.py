from main import stock


def do(operate):
    if "sync_stocks" == operate:
        stock.sync_stocks()
    if "sync_net_data" == operate:
        stock.sync_net_data()

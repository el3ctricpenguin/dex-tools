import ccxt

def getPrices(pair_name,lot=0.1,exchange_name='ftx'):
    exchange = eval('ccxt.'+exchange_name+'()')
    orderbook = exchange.fetch_order_book(pair_name)
    #bid = buy
    bid_price = totalOrderbook('bid',orderbook,lot)
    ask_price = totalOrderbook('ask',orderbook,lot)
    price_list = {'bid_price':bid_price[0],'bid_size':bid_price[1],'ask_price':ask_price[0],'ask_size':ask_price[1]}
    return price_list

#bidかaskを足し合わせる
#読みにくいが、売る時(bid)/買う時(ask)を同時にできるようにしている。
#dir(方向,str),orderbook(array),lot(float)を入力してロットの額まで板を足し合わせ、単位数で割る。
def totalOrderbook(dir,orderbook,lot): #dir=bid/ask
    total_dir_price = 0
    total_dir_size = 0
    for dir in orderbook[eval("dir+'s'")]:
        total_dir_price += dir[0]*dir[1]
        total_dir_size += dir[1]
        if total_dir_price >= lot:
            break
    dir_price_size = [total_dir_price/total_dir_size,total_dir_size]
    return dir_price_size

def convertUSDtoJPY(price_list):
    USDJPY = 115.8
    price_list['ask_price'] *= USDJPY
    price_list['bid_price'] *= USDJPY
    return price_list

if __name__ == '__main__':
    print('はじめに取引所名, 次に通貨ペア名(ex. BTC/USD,BTC/USDT)を入力')
    #例: ftx, BTC/USD
    exchange_name = input('exchange name?...')
    coin = input('coin/pair name?...')
    lot = 500 #どれくらい買いたいか(指定したペア建て)

    price_list = getPrices(coin.upper(),lot,exchange_name.lower())
    print('Ask Price: '+ str(price_list['ask_price']))
    print('Bid Price: '+ str(price_list['bid_price']))

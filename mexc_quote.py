import requests, json
#Rate limit: 20 times per second

#lot = 500
depth = 20 #板を何枚足し合わせるか

def get_url(token_buy):
    url = 'https://www.mexc.com/open/api/v2/market/depth?'+'symbol='+token_buy+'_USDT&depth='+str(depth)
    #print(url)
    return url

def get_prices(token,lot):
    response = requests.get(get_url(token))
    r = response.json() #jsonを辞書化
    output = {} #値段など結果を入れておく
    #print(r)
    #Buy price
    #平均購入価格を求めるため、lotの値段になるまで足し続ける
    total_buy_price = 0
    total_buy_quantity = 0
    for i in range(depth):
        total_buy_price += float(r['data']['asks'][i]['price'])*float(r['data']['asks'][i]['quantity'])
        total_buy_quantity += float(r['data']['asks'][i]['quantity'])
        if total_buy_price>lot:
            #print(i)
            break
    buyprice = total_buy_price/total_buy_quantity
    output['buy_price'] = buyprice
    output['buy_total'] = total_buy_price #ドル建てのロット
    #Sell price
    #平均購入価格を求めるため、lotの値段になるまで足し続ける
    total_sell_price = 0
    total_sell_quantity = 0
    for i in range(10):
        total_sell_price += float(r['data']['bids'][i]['price'])*float(r['data']['bids'][i]['quantity'])
        total_sell_quantity += float(r['data']['bids'][i]['quantity'])
        if total_sell_price>lot:
            break
    sellprice = total_sell_price/total_sell_quantity
    output['sell_price'] = sellprice
    output['sell_total'] = total_sell_price #ドル建てのロット
    #output += '\nsell price: 1' + token + ' = $' + str(round(sellprice,4)) + ' / ' + str(round(total_sell_price))
    return output


if __name__ == '__main__':
    lot=500
    print(get_prices('MCASH',lot))

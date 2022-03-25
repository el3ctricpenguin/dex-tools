import requests, json

chain_id = 137
token_addresses = {'MATIC':'0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee','USDT':'0xc2132D05D31c914a87C6611C10748AEb04B58e8F','MCASH':'0xa25610a77077390A75aD9072A084c5FbC7d43A0d'}
#lot = 500
usdt_decimals = 6

def start():
    with open('./1inch_tokenlist.json','r') as file:
        global token_addresses #グローバル変数を書き換えるときはきちんと宣言する。
        token_addresses = json.load(file)

def polygon(): #必要ないのだが形式的に。
    global chain_id
    chain_id = 137
    global usdt_decimals
    usdt_decimals = 6

def bsc():
    global chain_id
    chain_id = 56
    global usdt_decimals
    usdt_decimals = 18 #BSCのUSDTはdecimal 18

def get_quote(token_sell, token_buy, amount):
    url = 'https://api.1inch.exchange/v4.0/'+str(chain_id)+'/quote?'+'fromTokenAddress='+token_addresses[token_sell]+'&toTokenAddress='+token_addresses[token_buy]+'&amount='+str(amount)
    #print(url)
    return url

def get_prices(token, lot):
    #Buy price
    response = requests.get(get_quote('USDT',token,lot*10**usdt_decimals))
    r = response.json() #jsonを辞書化
    #print(r)
    output = {} #値段など結果を入れておく

    token_lot = int(r['toTokenAmount'])/(10**int(r['toToken']['decimals'])) #買えるトークンの数
    buyprice = lot/token_lot
    output['buy_price'] = buyprice
    output['buy_total'] = lot #ドル建てのロット
    #output = ' buy price: 1' + token + ' = $' + str(round(buyprice,4))

    #Sell price
    response = requests.get(get_quote(token,'USDT',r['toTokenAmount']))#token_lotでは整数にならない
    r = response.json() #jsonを辞書化
    usdt_lot = int(r['toTokenAmount'])/(10**int(r['toToken']['decimals']))
    sellprice = usdt_lot/token_lot

    output['sell_price'] = sellprice
    output['sell_total'] = lot #ドル建てのロット

    #output += '\nsell price: 1' + token + ' = $' + str(round(sellprice,4))
    return output

if __name__ == '__main__':
    lot=500
    print(get_prices('MCASH',lot))

import tushare as ts

def NameNumber(): 
    
    #tushare初始化
    ts.set_token('6996f4e55afd53fefa8c4caa9e89c4c097e772e72552c25b517f5b3c')
    pro = ts.pro_api()
    
    #获取并储存所有股票基本信息
    RawData = pro.stock_basic(exchange='', list_status='L', 
                           fields='ts_code,symbol,name,area,industry,list_date')
    data = RawData.to_dict('list')
    NameNumber = {}
    NameNumber['number'] = data['symbol']
    NameNumber['name'] = data['name']
    exchange = []
    for symbol in data['ts_code']:
        exchange.append(symbol[7:])  
    NameNumber['exchange'] = exchange

    return NameNumber
import baostock as bs
import pandas as pd
from search.models import NameNumber

# 返回关键数据
def search(number,start,end):

    ticker = NameNumber.objects.filter(number=number)
    for tic in ticker:
        name = tic.name
        exchange = tic.exchange + '.'

    try:
        #登陆baostock系统
        lg = bs.login()
        
        # 从网上获取历史数据
        StockRawHistory = bs.query_history_k_data_plus(exchange + number,
        "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",
        start_date=start, end_date=end, 
        frequency="d", adjustflag="2")
        StockHistoryList = []
        while StockRawHistory.next():
            StockHistoryList.append(StockRawHistory.get_row_data())
        StockHistory = pd.DataFrame(StockHistoryList, columns=StockRawHistory.fields)
        data = StockHistory.to_dict('list')
        
        #把有用的数据提取出来
        highs = data['high']
        for i in range(0,len(highs)):
            highs[i] = float(highs[i])
        lows = data['low']
        for i in range(0,len(lows)):
            lows[i] = float(lows[i])

        #计算价差大于0.02的日子有多少
        BigDays = 0
        for i in range(0,len(highs)):
            wave = (highs[i] - lows[i])/lows[i]
            if wave >= 0.02:
                BigDays += 1

        #计算各个区间段内运行的时间
        first = 0
        second = 0
        third = 0
        fourth = 0
        HighMax = max(highs)
        HighMin = min(highs)
        delta = (HighMax-HighMin)/4
        for high in highs:
            PeriodJug = (high-HighMin)/delta
            if PeriodJug<1:
                first += 1
                continue
            elif PeriodJug<2:
                second += 1
                continue
            elif PeriodJug<3:
                third += 1
                continue
            else:
                fourth += 1

        #计算四个区间范围
        stage_1 = [round(HighMin+delta*0,2),round(HighMin+delta*1,2)]
        stage_2 = [round(HighMin+delta*1,2),round(HighMin+delta*2,2)]
        stage_3 = [round(HighMin+delta*2,2),round(HighMin+delta*3,2)]
        stage_4 = [round(HighMin+delta*3,2),round(HighMin+delta*4,2)]

        #计算最大值,最小值和总天数
        low = round(min(lows),2)
        high = round(HighMax,2)
        days = len(highs)

        #登出系统
        bs.logout()

        return name,low,high,days,BigDays,first,stage_1,second,stage_2,third,stage_3,fourth,stage_4
    except:
        return '发生错误，请检查输入',0,0,0,0,0,[0,0],0,[0,0],0,[0,0],0,[0,0]
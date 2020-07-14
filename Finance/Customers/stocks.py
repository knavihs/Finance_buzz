from .models import Customer
from yahoo_fin.stock_info import get_data,get_day_gainers,get_day_losers
import pandas as pd



class Stocks_data:


    def latest_data(self,benutzer):
        try :
            companies_info = []
            customer = Customer.objects.filter(user=benutzer)
            for company in customer:
                C_name = str(company.companies_invested)
                ticker = get_data(C_name)
                df = pd.DataFrame(ticker,columns=['open','high','low','adjclose','volume'],dtype=float)
                df1 = df.tail(1)
                op = df1['open'].to_json()
                open = op[17:]
                hg = df1['high'].to_json()
                high = hg[17:]
                lo = df1['low'].to_json()
                low = lo[17:]
                cl = df1['adjclose'].to_json()
                close = cl[17:]
                vo = df1['volume'].to_json()
                volume = vo[17:]
                data = {
                    'name':company.companies_invested,
                    'open':open[:-1],
                    'high':high[:-1],
                    'low':low[:-1],
                    'close':close[:-1],
                    'volume':volume[:-1]
                }
                companies_info.append(data)
            return companies_info
        except AssertionError as error :
            print(error)


    def days_loser(self):
        loser = get_day_losers()
        df = pd.DataFrame(loser,columns=['Symbol','Price (Intraday)','Change','% Change'])
        df1= df.head(5)
        print(df1)
        data =[]
        for ind in df1.index:
            dic={
                'symbol':df1['Symbol'][ind],
                'price':df1['Price (Intraday)'][ind],
                'change':df1['Change'][ind],
                'per_change':df1['% Change'][ind]
            }
            data.append(dic)

        return data

    def days_gainer(self):
        gainer = get_day_gainers()
        df = pd.DataFrame(gainer,columns=['Symbol','Price (Intraday)','Change','% Change'])
        df1 = df.head(5)
        print(df1)
        data = []
        for ind in df1.index:
            dic = {
                'symbol': df1['Symbol'][ind],
                'price': df1['Price (Intraday)'][ind],
                'change': df1['Change'][ind],
                'per_change': df1['% Change'][ind]
            }
            data.append(dic)

        return data

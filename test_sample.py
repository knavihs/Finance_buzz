from alpha_vantage import timeseries,techindicators
import time
import pandas

'''api_key ='M4Q4ZCDA8C378UPD'
ts =timeseries.TimeSeries(key=api_key,output_format='pandas')
period= 60
data_ts = ts.get_intraday(symbol='MSFT',interval='1min',outputsize='compact')

df1= data_ts[0][period::10]



#df.index = pandas.Index()
print(df1)

ti = techindicators.TechIndicators(key=api_key,output_format='pandas')
data_ti,meta_data_ti = ti.get_rsi(symbol='MSFT',interval='1min',time_period=period,series_type='close')


df2= data_ti


print(df2)
total_df = pandas.concat([df1,df2],axis=1,sort=True)

print(total_df)'''

from yahoo_fin.stock_info import get_income_statement
msft = get_income_statement("MSFT")
print(msft)
df = pandas.DataFrame(msft,columns=['Breakdown','ttm','6/30/2019','6/30/2018','6/30/2017'])
print(df)

array=[]
for ind in df.index:
    data={
        'Breakdown':df['Breakdown'][ind],
        'Current':df['ttm'][ind],
        '2019':df['6/30/2019'][ind],
        '2018':df['6/30/2018'][ind],
        '2017':df['6/30/2017'][ind]
    }
    print(data)
    array.append(data)

print(array)







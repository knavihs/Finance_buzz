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





# -*- coding: utf-8 -*-
"""
Created on Sat May  8 23:02:23 2021

@author: abdou
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May  6 04:55:31 2021

@author: abdou
"""

import pandas as pd
import math
from datetime import datetime
import ccxt ,json
from ccxt import binance
import plotsend
from plotsend import *
import keys
import csv
import talib
import urllib
import matplotlib.pyplot as plt
import 
from talib import *
from time import time, sleep
from contextlib import contextmanager
import warnings
warnings.filterwarnings('ignore')
#import ast
dam=pd.DataFrame()
dan=pd.DataFrame()
#symbol=[ 'AAVE/USDT','ADA/USDT','AION/USDT','ALGO/USDT','ALPHA/USDT', 'AVAX/USDT', 'BNB/USDT','CHR/USDT', 'CHZ/USDT', 'COTI/USDT' ,'CRV/USDT','CTSI/USDT','DATA/USDT','DIA/USDT','DOGE/USDT','EGLD/USDT','ETH/USDT','FTM/USDT','IOTA/USDT' ,'MITH/USDT','REEF/USDT','STRAX/USDT','XRP/USDT','ZEC/USDT']
rsime=True
macdme=True
macdplusma=True
ma=True
#symbol=['NKN/USDT','PSG/USDT','COMP/USDT','COTI/USDT','ALPHA/USDT','DNT/USDT','ALGO/USDT','DIA/USDT', 'AVAX/USDT', 'BNB/USDT','BNT/USDT', 'CHZ/USDT' ,'CRV/USDT','CTSI/USDT','DATA/USDT','UTK/USDT','DOGE/USDT','REN/USDT','FTM/USDT','IOTA/USDT' ,'UNI/USDT','EPS/USDT','STRAX/USDT','XRP/USDT','ZEC/USDT','ORN/USDT' ,'THETA/USDT','GTO/USDT','DEGO/USDT','RIF/USDT' ,'WIN/USDT','WNXM/USDT','SAND/USDT','MATIC/USDT','RSR/USDT','CKB/USDT','STMX/USDT','ZIL/USDT','HBAR/USDT','OGN/USDT']   
symbol=['MBL/USDT','QTUM/USDT','KMD/USDT','ONT/USDT','BTS/USDT','BTT/USDT','COS/USDT','FUN/USDT','STPT/USDT','DOCK/USDT','DGB/USDT','PERL/USDT','TRX/USDT','ANKR/USDT','ROSE/USDT','IRIS/USDT','RVN/USDT','CTXC/USDT','CVC/USDT','GRT/USDT','WAN/USDT','PNT/USDT','KNC/USDT','ORN/USDT','1INCH/USDT','NULS/USDT','TCT/USDT','TWT/USDT','AION/USDT','OXT/USDT','TFUEL/USDT','ARPA/USDT','OGN/USDT','ZIL/USDT','RLC/USDT','TRB/USDT','FLM/USDT','SLP/USDT','DEGO/USDT', 'SRM/USDT','MKR/USDT','AUDIO/USDT','STORJ/USDT','CELO/USDT','DUSK/USDT','SXP/USDT','ONE/USDT','IOTX/USDT','ALPHA/USDT', 'AVAX/USDT','CHR/USDT', 'CHZ/USDT', 'COTI/USDT' ,'CRV/USDT','CTSI/USDT','DATA/USDT','DOGE/USDT','FTM/USDT','STRAX/USDT','XRP/USDT','EPS/USDT','FET/USDT','NKN/USDT','COMP/USDT','THETA/USDT','WNXM/USDT','RIF/USDT', 'WIN/USDT','SAND/USDT','MATIC/USDT','UNI/USDT']     
lstp1=pd.DataFrame()
lstp2=pd.DataFrame()
while True:
    sleep(5)
    for s in symbol:
        url = "http://www.kite.com"
        timeout = None
        try:
	        request = requests.get(url, timeout=timeout)
	        #print("Connected to the Internet")
        except (requests.ConnectionError, requests.Timeout) as exception:
	        print("No internet connection.")
    

        TA=pd.DataFrame()
        lastpoint=pd.DataFrame() 
  
        limit1=250
        
     

        exchange=ccxt.binance({
            'apiKey':keys.apiKey,
            'secret':keys.secretKey
    
        })
    
        market=exchange.load_markets()
        bars=exchange.fetch_ohlcv(s,'1m',limit=limit1)
        df = pd.DataFrame(bars, columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume'])
        df['Time']=[datetime.fromtimestamp(float(time)/1000) for time in df['Time']]
     
       




        macd, macdsignal, macdhist = talib.MACD(df['Close'], signalperiod=9)
        ma50=talib.MA(df['Close'],50)
        ma100=talib.MA(df['Close'],100)
        ma80=talib.MA(df['Close'],80)
        ma21=talib.MA(df['Close'],21)
        rsi=talib.RSI(df['Close'],timeperiod=14)
        
        TA['macd']=macd
        TA['macdsignal']=macdsignal
        TA['macdhist']=macdhist
        TA['ma50']=ma50
        TA['ma100']=ma100
        TA['ma80']=ma80
        TA['ma21']=ma21
        TA['rsi']=rsi



        #abd=calculations(df,TA,s)
        lastprice=exchange.fetch_ticker(s)
        lastp=float(lastprice['last'])
            
        n,m ,v,d=plotsend(df,TA,s,lastp,rsime,macdme,macdplusma,ma)
       # lastpoint=pd.DataFrame([])
       # lastpoint['Time']=xx
  
        #lastpoint['buyaround']=yy
  
       # lastpoint['sellat']=zz
    
        #lastpoint['stoploss']=sl
   

        
        #lastpoint.reset_index(drop=True, inplace=False)
        #lastpoint.set_index('Time')


   #     lastpoint=lastpoint.T
        
        
        

       # if (n==1): 
            
         #   link='https://api.telegram.org/bot1749382225:AAFm6D497qfMFkuwLTfUsCOPePGq9E1lvog/sendMessage?chat_id=-566915440&text= xxx-------coin : "{}"--------xxx'.format(s)
        #    requests.get(link)
       #     link1='https://api.telegram.org/bot1749382225:AAFm6D497qfMFkuwLTfUsCOPePGq9E1lvog/sendMessage?chat_id=-566915440&text="{}"'.format(lastpoint)
        #    requests.get(link1)
        if (n==1) or (m==1) or v==1 or d==1 :
            balance=exchange.fetch_balance()
            ss=s.split('/')
            ss=ss[0]

        if (n==1 or v==1 or d==1) and (balance['USDT']['free']>=50.5) and ((balance[ss]['free'])*lastp<20) and ((balance[ss]['used'])*lastp<5):
               ordre=exchange.create_market_buy_order(s, 50/lastp)
               market = exchange.market(s)
               balance=exchange.fetch_balance()
               amount=balance[ss]['free']
               price = ordre['price']*1.025
               stop_price = ordre['price']*0.98
               stop_limit_price =ordre['price']*0.98
               sleep(1)
               response = exchange.private_post_order_oco({
                      'symbol': market['id'],
                      'side': 'SELL',  # SELL, BUY
                      'quantity': exchange.amount_to_precision(s, amount),
                      'price': exchange.price_to_precision(s, price),
                      'stopPrice': exchange.price_to_precision(s, stop_price),
                      'stopLimitPrice': exchange.price_to_precision(s, stop_limit_price),  # If provided, stopLimitTimeInForce is required
                      'stopLimitTimeInForce': 'GTC',  # GTC, FOK, IOC
                       })
               aaa=[[s ,ordre['price'], price,stop_price,(price-ordre['price'])*100/ordre['price'],(stop_price-ordre['price'])*100/ordre['price']]]
               
               #print('macd methode',aaa)
               x=[]
               y=[]
               z=[]
               
               lastpoint=pd.DataFrame(aaa,columns=(['symbol','buyed at','sell price','stop','ifgain','ifloss']))   
               lstp1=lstp1.append(lastpoint)
               lastpoint=lastpoint.T

              
               
            

               link='https://api.telegram.org/bot1749382225:AAFm6D497qfMFkuwLTfUsCOPePGq9E1lvog/sendMessage?chat_id=-566915440&text= xxx----coin : "{}"----macd--xxx'.format(s)
               requests.get(link)
               link1='https://api.telegram.org/bot1749382225:AAFm6D497qfMFkuwLTfUsCOPePGq9E1lvog/sendMessage?chat_id=-566915440&text="{}"'.format(lastpoint)
               requests.get(link1)

               
              

              
               

         

        if (m==1) and (balance['USDT']['free']>=50.5) and ((balance[ss]['free'])*lastp<20) and ((balance[ss]['used'])*lastp<5):
               ordre=exchange.create_market_buy_order(s, 50/lastp)
               market = exchange.market(s)
               balance=exchange.fetch_balance()
               amount=balance[ss]['free']
               price = ordre['price']*1.025
               stop_price =  ordre['price']*0.98
               stop_limit_price = ordre['price']*0.98
               sleep(1)
               response = exchange.private_post_order_oco({
                      'symbol': market['id'],
                      'side': 'SELL',  # SELL, BUY
                      'quantity': exchange.amount_to_precision(s, amount),
                      'price': exchange.price_to_precision(s, price),
                      'stopPrice': exchange.price_to_precision(s, stop_price),
                      'stopLimitPrice': exchange.price_to_precision(s, stop_limit_price),  # If provided, stopLimitTimeInForce is required
                      'stopLimitTimeInForce': 'GTC',  # GTC, FOK, IOC
                       })
               aaa=[[s ,ordre['price'], price,stop_price,(price-ordre['price'])*100/ordre['price'],(stop_price-ordre['price'])*100/ordre['price']]]
               #print('rsi methode',aaa)
               x=[]
               y=[]
               z=[]
               lastpoint=pd.DataFrame(aaa,columns=(['symbol','buyed at','sell price','stop','ifgain','ifloss'])) 
               lstp2=lstp2.append(lastpoint)
               lastpoint=lastpoint.T
               #print(lstp2)

               link='https://api.telegram.org/bot1749382225:AAFm6D497qfMFkuwLTfUsCOPePGq9E1lvog/sendMessage?chat_id=-566915440&text= xxx---coin : "{}"-rsi-----xxx'.format(s)
               requests.get(link)
               link1='https://api.telegram.org/bot1749382225:AAFm6D497qfMFkuwLTfUsCOPePGq9E1lvog/sendMessage?chat_id=-566915440&text="{}"'.format(lastpoint)
               requests.get(link1)

               

    #print(lstp1)
    #print(lstp2)
    #header=['symbol','buyed at','sell price','stop']
    lstp1.to_csv('MA.csv')
    lstp2.to_csv('RSI.csv')
    print(lstp1)
    print(lstp2)
    lstp1,lstp2

       


               
               
               




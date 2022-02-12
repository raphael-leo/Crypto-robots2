# -*- coding: utf-8 -*-
"""
Created on Fri May 14 15:10:18 2021

@author: abdou
"""
import pandas as pd
import math
import ccxt
import keys 
import csv
import xlrd
abd=pd.DataFrame()
gainn=0

exchange=ccxt.binance({
    'apiKey':keys.apiKey,
    'secret':keys.secretKey
    
        })
lstp1=pd.read_excel('aa.xlsx')
#lstp1=pd.read_csv('bb.csv')
abd['symbol']=lstp1['Market']
abd['side']=lstp1['Type']
abd['amount']=lstp1['Total']
abd['fee']=lstp1['Fee']

ssb1=0
ssb2=0
do=0
ts=0
da=0
fees=0
b=[',']
for r,l,j in zip(abd['side'],(abd['amount']),abd['fee']):
    if r =='BUY':
        #y=l.split(',')
        c=l
        #c=(c.split('USDT'))[0]lst
        #c=(c.split('6')[0])
        ssb1=ssb1-(float(c))
        do=do+1
            
    elif r=='SELL':
        #y=l.split(',')
        c=l
        #c=(c.split('USDT'))[0]
        ssb2=ssb2+(float(c))
        da=da+1
        fees=fees+float(j)
ts=ssb1+ssb2
    #yy=j.split(',')
    #cc=yy[0][0:10]
    

print('gain dont be shock ',ts,fees)
        
        
    

          
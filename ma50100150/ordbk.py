# -*- coding: utf-8 -*-
"""
Created on Fri May 14 15:10:18 2021

@author: abdou
"""
import pandas as pd
import math
import ccxt
import keys 
abd=pd.DataFrame()
gain=0
symbol=['MBL/USDT','QTUM/USDT','KMD/USDT','ONT/USDT','BTS/USDT','BTT/USDT','COS/USDT','FUN/USDT','STPT/USDT','DOCK/USDT','DGB/USDT','PERL/USDT','TRX/USDT','ANKR/USDT','ROSE/USDT','IRIS/USDT','RVN/USDT','CTXC/USDT','CVC/USDT','GRT/USDT','WAN/USDT','PNT/USDT','KNC/USDT','ORN/USDT','1INCH/USDT','NULS/USDT','TCT/USDT','TWT/USDT','AION/USDT','OXT/USDT','TFUEL/USDT','ARPA/USDT','OGN/USDT','ZIL/USDT','RLC/USDT','TRB/USDT','FLM/USDT','SLP/USDT','DEGO/USDT', 'SRM/USDT','MKR/USDT','AUDIO/USDT','STORJ/USDT','CELO/USDT','DUSK/USDT','SXP/USDT','ONE/USDT','IOTX/USDT','ALPHA/USDT', 'AVAX/USDT','CHR/USDT', 'CHZ/USDT', 'COTI/USDT' ,'CRV/USDT','CTSI/USDT','DATA/USDT','DOGE/USDT','FTM/USDT','STRAX/USDT','XRP/USDT','EPS/USDT','FET/USDT','NKN/USDT','COMP/USDT','THETA/USDT','WNXM/USDT','RIF/USDT', 'WIN/USDT','SAND/USDT','MATIC/USDT','UNI/USDT'] 
exchange=ccxt.binance({
    'apiKey':keys.apiKey,
    'secret':keys.secretKey
    
        })
def gain(exchange,symbol,limit):
    ts=0

    if exchange.has['fetchMyTrades']:
             zz=exchange.fetch_my_trades(symbol=symbol,limit=limit, params={})
             zz=pd.DataFrame(zz)

    abd['symbol']=zz['symbol']
    abd['side']=zz['side']
    abd['amount']=zz['amount']
    abd['cost']=zz['cost']
    abd['fee']=zz['fee'][:]
    ssb=0
    do=0
    da=0
    for r,l in zip(abd['side'],abd['cost']):
        if r=='buy':
            ssb=ssb+l
            do=do+1
            ts=ts+ssb
        elif r =='sell':
            ssb=ssb-l
            da=da+1
            ts=ts+ssb
        
        
    return ts,da,do

for s in symbol:
    ts,da,do=gain(exchange,s,2)
    gain=gain+ts
print(gain)
          
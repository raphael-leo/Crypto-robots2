# -*- coding: utf-8 -*-
"""
Created on Sat May  8 23:06:44 2021

@author: abdou
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May  6 05:00:51 2021

@author: abdou
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 17:07:18 2021

@author: abdo
"""
import pandas as pd
import math
def plotsend(dx,indicators,s,lastp,rsime,macdme,macdplusma,mame):
    n=0
    m=0
    xx=[]
    yy=[]
    zz=[]
    sl=[]
    cd=0
    cd1=0
    cd2=0
    cd3=0
    w=0
    v=0
    d=0
    

    
    for q,w in zip(indicators['macd'].tail(5).iloc[0:3],indicators['macdsignal'].tail(5).iloc[0:3]):
            if q<w<=0:
                cd=cd+1
    #print(cd)
 
    for k,j in zip(indicators['ma100'].tail(5),dx['Close'].tail(5)):
        if k<=j:
            cd1=cd1+1
    #print(cd,cd1,cd2)   
    if dx['Close'].iloc[-1]>=indicators['ma80'].iloc[-1]  :
        cd2=1
     
    
 
    
    
    if  macdme==True  and cd>=2 and indicators['rsi'].iloc[-1]>=30 and cd1>=0 and cd2>=0 and (indicators['macd'].iloc[-1]>indicators['macdsignal'].iloc[-1] or indicators['macd'].iloc[-2]>=indicators['macdsignal'].iloc[-2]) :
            n=1
            m=0
    
    if rsime==True and indicators['rsi'].iloc[-1]<23 : #and dx['Close'].iloc[-1]<indicators['ma100'].iloc[-1]:
        m=1
        n=0
    if macdplusma==True  and cd>=2 and cd1>=1 and (indicators['macd'].iloc[-1]>indicators['macdsignal'].iloc[-1]):
       v=1
       d=0
    for l,h in zip(indicators['ma21'].tail(5),dx['Close'].tail(5)):
        if l>h:
            w=w+1
    if mame==True and w>=2 and indicators['ma21'].iloc[-1]<dx['Close'].iloc[-1]:
        v=0
        d=1


                #print(yy)
                 

    return n,m,v,d

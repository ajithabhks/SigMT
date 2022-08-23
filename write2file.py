# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:19:53 2020

@author: AJITHABH K. S.
Last modified: 21-07-2022

This script helps to create a text file with all impedance values, tipper data and variances.

This is required because, processing is done for data with different sampling frequencies. So,
text file need to be created with data of each target frequencies (For e.g. 1024 Hz). After
processing all data, join the text files to create a final text file contains data for all target
frequencies.

Then it can be converted to EDI format using 'write2edi-data.py' script.

Give path to save the text file with a filename in variable 'f'.

If the sampling frequency is 1024 Hz, give filename as '1024Hz.txt'

Read usermanual for more details.
"""

ftlist = ftlist
ZxxR = np.real(Zxx_huber)
ZxxI = np.imag(Zxx_huber)
ZxyR = np.real(Zxy_huber)
ZxyI = np.imag(Zxy_huber)
ZyxR = np.real(Zyx_huber)
ZyxI = np.imag(Zyx_huber)
ZyyR = np.real(Zyy_huber)
ZyyI = np.imag(Zyy_huber)
ZxxVar = Zvar.get('xx')
ZxyVar = Zvar.get('xy')
ZyxVar = Zvar.get('yx')
ZyyVar = Zvar.get('yy')
TxR = np.real(Tx)
TxI = np.imag(Tx)
TyR = np.real(Ty)
TyI = np.imag(Ty)
f = open('C:/Users/Ajithabh/Desktop/Outputs/KL33A/bands/1024Hz.txt', 'w')
for i in range(ftlist.shape[0]):
    f.write("%.9E \t %.9E  \t %.9E \t %.9E \t %.9E \t %.9E \t %.9E \t %.9E \t %.9E \t %.9E \t %.9E \t %.9E \t %.9E \t %.9E \t %.9E \t %.9E \t %.9E \t %.9E \t %.9E \n" % (ftlist[i][0],
    ZxxR[i][0], ZxxI[i][0], ZxyR[i][0], ZxyI[i][0],ZyxR[i][0], ZyxI[i][0],ZyyR[i][0], 
    ZyyI[i][0], ZxxVar[i][0], ZxyVar[i][0], ZyxVar[i][0], ZyyVar[i][0],
    TxR[i][0],TxI[i][0],TyR[i][0],TyI[i][0],TxVar[i][0],TyVar[i][0]))
f.close()
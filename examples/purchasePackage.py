# -*- coding: utf-8 -*-
from xlpy import *

xl = XL('MSISDN/NO.TELP')
r = xl.loginWithOTP('OTP Code')
if(r != False):
    s = xl.purchasePackage('Service ID')
    print(s['message'])
else:
    print("Login failed try again")

# -*- coding:utf-8 -*-
from Api.LicesenCommon import *
if __name__ == '__main__':
    licesens=LicesenMethod()
    res=licesens.createLicesen("123","888")
    licesens.deleteLicesen("123","888",res)
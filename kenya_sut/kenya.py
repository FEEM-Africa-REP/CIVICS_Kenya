# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:07:09 2020

@author: nigolred
"""
import civivs_sut as cvx

kenya = cvx.C_SUT(r'Database\Kenya_2014_SAM.xlsx')

Z = kenya.Z
VA = kenya.VA
Y = kenya.Y
GO = kenya.GO
HH = kenya.HH
IN = kenya.IN
X = kenya.X
GVA = kenya.F.sum().sum()
Margins = kenya.F_M

#%%
kenya.shock(path = r'Database\Shock.xlsx' , Z = False,Y=True )
#%%
kenya.calc_all()
#%%
kenya.aggregate()
X = kenya.X_agg
VA = kenya.VA_agg
Y = kenya.Y_agg
Z = kenya.Z_agg

ROW = Z.sum(axis=1) + VA.sum(axis=1)
#%%
kenya.Save_all(path=r'C:\Users\Amin\Documents\GitHub\My Kenya\kenya_sut\Result')
#%%

a=kenya.S
b=kenya.S_c_agg
#%%
S = b.drop('unused')

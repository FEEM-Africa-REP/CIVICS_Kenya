# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:12:58 2020

@author: Mohammad Amin Tahavori
"""
import time
start = time.time()
import calliope
import pickle
try:
    calliope.set_log_level('INFO')
except:
    calliope.set_log_verbosity('INFO')
model = calliope.Model('model.yaml')
model.run()
end=time.time()
print(str(end-start))
#%%
import cal_graph as CG
amin=CG.C_Graph(model=model,ex_path=r'Graph_inputs.xlsx',unit='kW')
# with open('cof_4n', 'wb') as config_dictionary_file:
# 	pickle.dump(amin,config_dictionary_file)
#%%
amin.system_pie(kind='absolute',unit='GWh',v_round=1,title_font=40)
#%%
amin.node_pie(kind='absolute',unit='GWh',v_round=1,title_font=40)
#%%
amin.node_pie(kind='absolute',unit='GWh',v_round=1,title_font=40,rational='consumption')


#%%
amin.sys_dispatch(unit='MW',sp_techs='bio_coffee_pp',average='weekly',x_ticks='name')
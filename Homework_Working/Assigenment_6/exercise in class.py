# %%
import numpy as np
import pandas as pd

# %%
data= np.ones((7,3))
data_frame =pd.DataFrame(data,columns=['data1','data2','data3'],index=['a','b','c','d','e','f','g'])
# %%
data_frame.loc[['a','e']] = 3
# %%
data_frame.loc[['a','b','c','d']]*7
# %%
data_frame2 = data_frame
data_frame2.loc[['a','c','e','g'],['data1','data3']] = 0
data_frame2.loc[['b','d','f'],['data2']] = 1
# %%
data_frame3 = data_frame
data_frame3.iloc[0:8:2,0:3:2] = 0
data_frame3.iloc[1:8:2, 1:3:2]= 1
# %%

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle

loaded_model=pickle.load(open("C:/125156105/multiple disease prediction/trained_model.sav",'rb'))
scaler=StandardScaler()

input_data=(6,148,72,35,0,33.6,0.627,50)
inp_num=np.asarray(input_data) #changing input_data to numpy array
reshaped=inp_num.reshape(1,-1)
std_data=scaler.fit_transform(reshaped)
pred=loaded_model.predict(std_data)

print(pred)
if pred==1:
    print('Person is diabetic')
else:
    print('Person does not have diabetes')

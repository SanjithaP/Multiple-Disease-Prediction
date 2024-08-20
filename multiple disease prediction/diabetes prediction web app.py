# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 16:35:14 2024

@author: Sanjitha
"""

import numpy as np
import pickle
import streamlit as sp
from sklearn.preprocessing import StandardScaler

#loading the model
loaded_model=pickle.load(open("C:/125156105/multiple disease prediction/Deploying model/trained_model.sav",'rb'))
scaler=StandardScaler()
#creating a function for prediction
def diabetes_prediction(input_data):
    inp_num=np.asarray(input_data) #changing input_data to numpy array
    reshaped=inp_num.reshape(1,-1)
    scaler.fit(reshaped)
    std_data=scaler.transform(reshaped)
    print(std_data)
    pred=loaded_model.predict(std_data)

    print(pred)
    if pred==1:
        return 'Person is diabetic'
    else:
        return 'Person is not diabetic'
    
def main():
    #giving a tittle
    sp.title('Diabetes prediction web app')
    
    #getting the input data from user
    								
    Pregnancies = sp.text_input('Number of Pregnancies')
    Glucose = sp.text_input('Glucose level')
    BloodPressure = sp.text_input('Blood Pressure value')
    SkinThickness = sp.text_input('Skin Thickness value')
    Insulin = sp.text_input('Insulin level')
    BMI = sp.text_input('BMI')
    DiabetesPedigreeFunction = sp.text_input('Diabetes Pedigree Function value')
    Age = sp.text_input('Age of the person')
    
    #code for prediction
    diagnosis = ''
    #create button for prediction
    if sp.button('Diabetes test result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    sp.success(diagnosis)
    
if __name__=='__main__':
    main()
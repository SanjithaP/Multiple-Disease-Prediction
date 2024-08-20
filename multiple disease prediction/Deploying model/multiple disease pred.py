# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:34:46 2024

@author: Sanjitha
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models
diabetes_model=pickle.load(open('C:/125156105/multiple disease prediction/Deploying model/saved models/diabetes_model.sav','rb'))
heart_model=pickle.load(open('C:/125156105/multiple disease prediction/Deploying model/saved models/heart_model.sav','rb'))
parkinson_model=pickle.load(open('C:/125156105/multiple disease prediction/Deploying model/saved models/parkinson_model.sav','rb'))

#side bar or navigation
with st.sidebar:
    selected = option_menu('Multiple disease prediction system',
                           ['Diabetes Prediction', 
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons = ['activity','heart','person'],
                           default_index=0)
    
#diabetes prediction page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    
    #columns for input
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
        
    with col2:
        Insulin = st.text_input('Insulin level')
        
    with col3:
        BMI = st.text_input('BMI')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        
    with col2:
        Age = st.text_input('Age of the person')
        
    
    #code for prediction
    diab=''
    #create a button for prediction
    if st.button('Diabetes test result'):
        diab_pred=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if diab_pred[0]==1:
            diab = 'The person is diabetic'
        else:
            diab = 'The person is not diabetic'
            
    st.success(diab)

if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age of the person')
        
    with col2:
        sex = st.text_input('Gender of the person')
        
    with col3:
        cp = st.text_input('Chest pain type')
        
    with col1:
        trestbps = st.text_input('Resting blood pressure')
    
    with col2:
        chol = st.text_input('Serum cholestrol in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting blood sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic result')
        
    with col2:
        thalach = st.text_input('Maximum heart rate achieved')
        
    with col3:
        exang = st.text_input('Exercise induced angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced ny exercise')
    
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flouroscopy')
        
    with col1:
        thal = st.text_input('Thal:0 = normal; 1 = fixed defect; 2=reversable defect' )
        
    #code for prediction
    heart=''
    #create a button for prediction
    if st.button('Diabetes test result'):
        heart_pred=heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if heart_pred[0]==1:
            heart = 'The person is having heart disease'
        else:
            heart = 'The person is not having heart disease'
            
    st.success(heart)
    
    
       
if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Prediction using ML')
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        fo = st.text_input('MDVP: Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP: Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP: Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP: Jitter(%)')
    
    with col5:
        Jitter_abs = st.text_input('MDVP: Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP: RAP')
        
    with col2:
        PPQ = st.text_input('MDVP: PPQ')
        
    with col3:
        DDP = st.text_input('Jitter: DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP: Shimmer')
        
    with col5:
        db = st.text_input('MDVP: Shimmer(dB)')
    
    with col1:
        APQ3 = st.text_input('Shimmer: APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer: APQ5')
        
    with col3:
        APQ = st.text_input('MDVP: APQ' )
        
    with col4:
        DDA = st.text_input('Shimmer: DDA')
        
    with col5:
        NHR = st.text_input('NHR')
    
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA' )
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
    #code for prediction
    park=''
    #create a button for prediction
    if st.button('Diabetes test result'):
        park_pred=heart_model.predict([[fo,fhi,flo,Jitter_percent ,Jitter_abs,RAP,PPQ,DDP,Shimmer,db,APQ3,APQ5,APQ,DDA,NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        
        if park_pred[0]==1:
            park = 'The person is suffering from parkinsons disease'
        else:
            park = 'The person is not having parkinsons disease'
            
    st.success(park)
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 17:25:37 2025

@author: sraja
"""


import pickle 
import streamlit as st
from streamlit_option_menu import option_menu


# loading the models 

diabetes_model = pickle.load(open('trained_model.sav','rb'))

heart_disease_model = pickle.load(open('heart_model (4).sav','rb'))


# sidebar for navigation 

with st.sidebar:
    
    
    
    selected = option_menu('Multiple Dieases Prediction System',
                       ['Diabetes Prediction', 'Heart Disease Prediction'],
                       icons =['activity', 'heart-fill'],
                       default_index = 0)

    
    # diabetes prediction satge 
if (selected == 'Diabetes Prediction'):
    # input of the data 
    st.title('Diabetes Presdiction using ML')
     
    
    # getting the input from the user 
    col1, col2, col3 =st.columns(3)
    
    with col1:
        Pregnancies  =st.text_input('Number of Pregnancies')
    with col2:
        Glucose= st.text_input('Glucose level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')
        
        
        
        
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)
    
    
    
    
    
    
if (selected == 'Heart Disease Prediction'):
    
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
    def safe_float(value):
        
        try:
          return float(value)
        except ValueError:
          return 0.0  # or raise an error, or show a warning
    
  

     
    # code for Prediction
    heart_diagnosis= ''
    
    # creating button for prediction 
    if st.button('Heart Disease Test Result'):
        
        
        heart_prediction = heart_disease_model.predict([[safe_float(age), safe_float(sex), safe_float(cp), safe_float(trestbps),safe_float(chol), safe_float(fbs), safe_float(restecg),
                                                     safe_float(thalach),safe_float(exang), safe_float(oldpeak),safe_float(slope), safe_float(ca), safe_float(thal)]])

       
        if(heart_prediction[0]==1):
            heart_diagnosis ='The Person Have Heart Disease'
            
            
        else:
            heart_diagnosis ='The Person Does Not have any Heart Disease'
            
    st.success(heart_diagnosis)
        
                   
        
        
    
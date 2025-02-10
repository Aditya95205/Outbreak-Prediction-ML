import os
import pickle  # For loading the model
import streamlit as st # For the web app
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Prediction of Disease Outbreaks", page_icon="👨🏻‍⚕", layout="wide")

working_dir = os.path.dirname(os.path.abspath(__file__))

diabetes_model = pickle.load(open(r"C:\Users\KIIT\OneDrive\Desktop\Outbreak-Prediction-ML\Models\diabetes_model.sav", 'rb'))
heart_model = pickle.load(open(r"C:\Users\KIIT\OneDrive\Desktop\Outbreak-Prediction-ML\Models\heart_model.sav", 'rb'))
parkinson_model = pickle.load(open(r"C:\Users\KIIT\OneDrive\Desktop\Outbreak-Prediction-ML\Models\parkinsons_model.sav", 'rb'))

with st.sidebar:
        #disease=option_menu("Select Disease",
                          #   ["Diabetes","Heart Disease","Parkinson's Disease"],menu_icon='hospital-fill',icons=['activity', 'heart', 'person'],default_index=0)
   # st.title("Prediction of Disease Outbreaks")
    #st.write("Select the disease you want to predict")
    disease = option_menu("Disease", 
                         ["Diabetes", "Heart Disease", "Parkinson's Disease"],
                          menu_icon='hospital-fill',icons=['activity', 'heart', 'person'], default_index=0)
if disease == "Diabetes":
        st.title("You selected Diabetes")
        col1, col2,col3 = st.columns(3)
        with col1:
            pregnancies = st.text_input('Number of Pregnancies')
        with col2:    
            glucose = st.text_input("Glucose Level")
        with col3:
            blood_pressure = st.text_input("Blood Pressure")
        with col1:
                skin_thickness = st.text_input("Skin Thickness")
        with col2:
                insulin = st.text_input("Insulin")
        with col3:
                bmi = st.text_input("BMI")
        with col1:
                diabetes_pedigree_function = st.text_input("Diabetes Pedigree Function")
        with col2:
                age = st.text_input("Age")

diab_diagnosis = ''
if st.button("Predict Diabetes"):
    user_input = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]
    user_input=[float(x) for x in user_input]
    diab_prediction = diabetes_model.predict([user_input])
    if diab_prediction[0] == 0:
        diab_diagnosis='You are not diabetic'
    else:
        diab_diagnosis='You are diabetic'
st.success(diab_diagnosis)        
st.write("Made by: Aditya Gupta")                                                   

#disease = option_menu("Disease", 
                        # ["Diabetes", "Heart Disease", "Parkinson's Disease"],
                         # menu_icon='hospital-fill',icons=['activity', 'heart', 'person'], default_index=0)
if disease == "Heart Disease":
        st.title("You selected Heart Disease")
        col1, col2,col3 = st.columns(3)
        with col1:
            age = st.text_input("age")
        with col2:    
            sex = st.text_input("sex")
        with col3:
            cp = st.text_input("cp")
        with col1:
                trestbps = st.text_input("trestbps")
        with col2:
                chol = st.text_input("chol")
        with col3:
                fbs = st.text_input("fbs")
        with col1:
                restecg = st.text_input("restecg")
        with col2:
                oldpeak = st.text_input("oldpeak")
        with col3:
                thalach = st.text_input("thalach")     
        with col1:
                slope = st.text_input("slope")    
        with col2:
                ca = st.text_input("ca")  
        with col3:
                thal = st.text_input("thal")                       

heart_diagnosis =''
if st.button("Predict Heart Disease"):
   user_input = [age, sex, cp, trestbps, chol, fbs, restecg, oldpeak, thalach, slope, ca, thal]
   user_input=[float(x) for x in user_input]
   heart_prediction = heart_model.predict([user_input])
   if heart_prediction[0] == 0:
       heart_diagnosis='You are not heart patient'
   else:
        heart_diagnosis='You are heart patient'
st.success(heart_diagnosis)      
st.write("Made by: Aditya Gupta")   

if disease == "Parkinson's Disease":
        st.title("You selected Parkinson's Disease")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            MDVP_Fo = st.number_input("MDVP_Fo(Hz)")
        with col2:    
            MDVP_Fhi = st.number_input("MDVP_Fhi(Hz)")
        with col3:
            MDVP_Flo = st.number_input("MDVP_Flo(Hz)")
        with col4:
                MDVP_Jitter = st.number_input("MDVP_Jitter")
        with col5:
                MDVP_Shimmer = st.number_input("MDVP_Shimmer")
        with col1:
                NHR = st.number_input("NHR")
        with col2:
                HNR = st.number_input("HNR")
        with col3:
                RPDE = st.number_input("RPDE")
        with col4:
                DFA = st.number_input("DFA")
        with col5:
                spread1 = st.number_input("spread1")
        with col1:
                spread2 = st.number_input("spread2")
        with col2:
                D2 = st.number_input("D2")
        with col3:
                PPE = st.number_input("PPE")
                
parkinson_diagnosis = ''
   
if st.button("Predict Parkinson's Disease"):
       user_input = [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Shimmer, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
       user_input=[float(x) for x in user_input]
       parkinson_prediction = parkinson_model.predict([user_input])
       if parkinson_prediction[0] == 0:
           parkinson_diagnosis='You are not parkinson patient'
       else:
           parkinson_diagnosis='You are parkinson patient'  
st.success(parkinson_diagnosis)
st.write("Made by: Aditya Gupta")                 
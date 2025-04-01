import streamlit as st
import joblib
st.title('HEART DISEASE PREDICTION')
model= joblib.load('Heart_Disease_Prediction.joblib')
Age= st.number_input('Enter age')
Sex= st.number_input('Enter gender (M:1,FM:0)')
Chest pain type= st.number_input('Enter in digits')
BP= st.number_input('Enter blood pressure')
Cholesterol= st.number_input('Enter cholesterol')
FBS over 120= st.number_input('Enter FBS(Y:1,N:0)')
EKG results= st.number_input('Enter in digits')
MAX HR= st.number_input('Enter max hr')
Exercise agina = st.number_input('Enter exercise agina(Y:1,N:0)')
ST depression= st.number_input('Enter st depression')
Slope of ST= st.number_input('Enter slope of st')
Number of vessels fluro= st.number_input('Enter no of vesselsfluro')
Thallium= st.number_input('Enter thallium percentage')
if st.button('Predict Heart Disease'):
    prediction=model.predict([[Age,Sex,Chest pain type,BP,Cholestrol,FBS over 120,EKG results,MAX HR,Exercise agina,ST depression,Slope of ST,Number of vessels fluro,Thallium]])
    if prediction=='Y':
        st.text('Heart disease presence')
    else:
        st.text('Heart disease absence')

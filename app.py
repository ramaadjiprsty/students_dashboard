# streamlit_app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder
from mappings import mappings

st.set_page_config(page_title='Dropout Risk Predictor', layout='wide')

# Load model
@st.cache_resource()
def load_model(path='model/final_logistic_model.pkl'):
    return joblib.load(path)

model = load_model()

# Label encoder
le = LabelEncoder()
le.classes_ = np.array(['Dropout', 'Enrolled', 'Graduate'])

# Feature columns
feature_cols = [
    'Marital_status','Application_mode','Application_order','Course',
    'Daytime_evening_attendance','Previous_qualification','Previous_qualification_grade',
    'Nacionality','Mothers_qualification','Fathers_qualification',
    'Mothers_occupation','Fathers_occupation','Admission_grade','Displaced',
    'Educational_special_needs','Debtor','Tuition_fees_up_to_date','Gender',
    'Scholarship_holder','Age_at_enrollment','International',
    'Curricular_units_1st_sem_credited','Curricular_units_1st_sem_enrolled',
    'Curricular_units_1st_sem_evaluations','Curricular_units_1st_sem_approved',
    'Curricular_units_1st_sem_grade','Curricular_units_1st_sem_without_evaluations',
    'Curricular_units_2nd_sem_credited','Curricular_units_2nd_sem_enrolled',
    'Curricular_units_2nd_sem_evaluations','Curricular_units_2nd_sem_approved',
    'Curricular_units_2nd_sem_grade','Curricular_units_2nd_sem_without_evaluations',
    'Unemployment_rate','Inflation_rate','GDP'
]

engineered_cols = ['avg_sem_grade','total_units_approved']
all_features = feature_cols + engineered_cols


st.title('📊 Student Dropout Risk Predictor')
st.markdown("Aplikasi ini memprediksi risiko mahasiswa **Dropout**, **Graduate**, atau **Enrolled** berdasarkan data akademik dan demografis.")

# Input UI
st.subheader("Masukkan Data Mahasiswa")
col1, col2, col3 = st.columns(3)
inputs = {}

for i, col in enumerate(feature_cols):
    current_col = [col1, col2, col3][i % 3]
    with current_col:
        if col in mappings and mappings[col]:
            options = list(mappings[col].keys())
            inputs[col] = st.selectbox(col, options, format_func=lambda x: mappings[col][x])
        elif col in ['Previous_qualification_grade','Admission_grade',
                     'Curricular_units_1st_sem_grade','Curricular_units_2nd_sem_grade',
                     'Unemployment_rate','Inflation_rate','GDP']:
            inputs[col] = st.number_input(col, value=0.0)
        else:
            inputs[col] = st.number_input(col, value=0)

input_df = pd.DataFrame([inputs])
input_df['avg_sem_grade'] = (input_df['Curricular_units_1st_sem_grade'] + input_df['Curricular_units_2nd_sem_grade']) / 2
input_df['total_units_approved'] = input_df['Curricular_units_1st_sem_approved'] + input_df['Curricular_units_2nd_sem_approved']

st.subheader("Data Input")
st.write(input_df)

if st.button("🔍 Prediksi Risiko Dropout"):
    preds_int = model.predict(input_df[all_features])
    preds_label = le.inverse_transform(preds_int)
    color = 'red' if preds_label[0]=='Dropout' else ('green' if preds_label[0]=='Graduate' else 'blue')
    st.subheader("Hasil Prediksi")
    st.markdown(f"<span style='color:{color}; font-size:24px; font-weight:bold'>{preds_label[0]}</span>", unsafe_allow_html=True)

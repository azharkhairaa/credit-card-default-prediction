import streamlit as st
import joblib
import pandas as pd

# load
model = joblib.load("model.pkl")

# mapping education_level
education_mapping = {
    "Graduate School": 1,
    "High School": 3,
    "University": 2,
    "Others": 4
}

# mapping repayment status
repayment_mapping = {
    "No Bill": -2,
    "Pay Duly and Full Payment": 1,
    "Pay Duly": 0,
    "1 month late": 1,
    "2 months late": 2,
    "3 months late": 3,
    "4 months late": 4,
    "5 months late": 5,
    "6 months late": 6,
    "7 months late": 7,
    "8 months late": 8,
}

# mapping prediction
def predict_label(predictions):
    return ["Default Payment" if x == 1 else "Non-Default Payment" for x in predictions]

# app
def main():
    st.title("Credit Risk Prediction")
    st.write("Hacktiv8 - Phase 1 - Full Time Data Analytics")
    st.write("Graded Challenge 5 - RMT 033 - Muhammad Azhar Khaira")

    st.sidebar.header("User Input Features")

    # input features
    limit_balance = st.sidebar.number_input("Limit Balance", value=67919.0)

    education_level_text = st.sidebar.selectbox(
        "Education Level",
        options=list(education_mapping.keys()),
        index=0
    )
    education_level = education_mapping[education_level_text]

    pay_0_text = st.sidebar.selectbox(
        "Repayment Status in September",
        options=list(repayment_mapping.keys()),
        index=0
    )
    pay_0 = repayment_mapping[pay_0_text]

    pay_2_text = st.sidebar.selectbox(
        "Repayment Status in August",
        options=list(repayment_mapping.keys()),
        index=0
    )
    pay_2 = repayment_mapping[pay_2_text]

    pay_3_text = st.sidebar.selectbox(
        "Repayment Status in July",
        options=list(repayment_mapping.keys()),
        index=0
    )
    pay_3 = repayment_mapping[pay_3_text]

    pay_4_text = st.sidebar.selectbox(
        "Repayment Status in June",
        options=list(repayment_mapping.keys()),
        index=0
    )
    pay_4 = repayment_mapping[pay_4_text]

    pay_5_text = st.sidebar.selectbox(
        "Repayment Status in May",
        options=list(repayment_mapping.keys()),
        index=0
    )
    pay_5 = repayment_mapping[pay_5_text]

    pay_6_text = st.sidebar.selectbox(
        "Repayment Status in April",
        options=list(repayment_mapping.keys()),
        index=0
    )
    pay_6 = repayment_mapping[pay_6_text]

    pay_amt_1 = st.sidebar.number_input("Amount of previous payment in September", value=20000.0)
    pay_amt_2 = st.sidebar.number_input("Amount of previous payment in August", value=15000.0)
    pay_amt_3 = st.sidebar.number_input("Amount of previous payment in July", value=10000.0)
    pay_amt_4 = st.sidebar.number_input("Amount of previous payment in June", value=22500.0)
    pay_amt_5 = st.sidebar.number_input("Amount of previous payment in May", value=50000.0)
    pay_amt_6 = st.sidebar.number_input("Amount of previous payment in April", value=20000.0)

    if st.sidebar.button("Submit"):
        # Data
        input_data = pd.DataFrame([{
            'limit_balance': limit_balance,
            'education_level': education_level,
            'pay_0': pay_0,
            'pay_2': pay_2,
            'pay_3': pay_3,
            'pay_4': pay_4,
            'pay_5': pay_5,
            'pay_6': pay_6,
            'pay_amt_1': pay_amt_1,
            'pay_amt_2': pay_amt_2,
            'pay_amt_3': pay_amt_3,
            'pay_amt_4': pay_amt_4,
            'pay_amt_5': pay_amt_5,
            'pay_amt_6': pay_amt_6
        }])

        st.subheader("Data Input")
        st.write(input_data)

        # proses prediksi
        predictions = model.predict(input_data)
        mapped_predictions = predict_label(predictions)

        # show prediksi
        st.subheader("Prediction Result")
        st.subheader(mapped_predictions[0])

if __name__ == "__main__":
    main()

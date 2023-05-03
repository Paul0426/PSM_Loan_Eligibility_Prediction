import streamlit as st
import pickle
import numpy as np
import pandas as pd


def main():
    bg = """
        <div style='background-color:LightGray; padding:13px; display:flex; align-items:center; color:black;'>
            <img src="https://iili.io/Hv60FWv.md.jpg" alt="Your Image" width="150" style='margin-right:10px;'>
            <h1 style='color:black; text-align:center;'>Loan Eligibility Prediction</h1>
        </div>
    """
    st.markdown(bg, unsafe_allow_html=True)

    left, right = st.columns((2, 2))
    Gender = left.selectbox('Gender', ('Male', 'Female'))

    Married = right.selectbox('Married', ('Yes', 'No'))

    Dependents = left.selectbox('Dependents', ('None', 'One', 'Two', 'Three or More'))

    Education = right.selectbox('Education', ('Graduate', 'Not Graduate'))

    Self_Employed = left.selectbox('Self-Employed', ('Yes', 'No'))

    ApplicantIncome = right.number_input("Applicant Income", value=0)

    CoapplicantIncome = left.number_input("Coapplicant Income", value=0)

    LoanAmount = right.number_input("Loan Amount (Thousands)", value=0)

    Loan_Amount_Term = left.number_input("Loan Tenor (Months)", value=0)

    Credit_History = right.number_input('Credit History', 0, 1)

    Property_Area = st.selectbox('Property Area', ('Semiurban', 'Urban', 'Rural'))

    button = st.button('Predict')

    # if button is clicked
    if button:
        # make prediction
        result = predict(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome,
                         CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area)

        if result == 'ELIGIBLE':
            st.success(f'You are {result} for the loan')
        else:
            st.error(f'You are {result} for the loan')


# load the train model
with open('train_model.pkl', 'rb') as pkl:
    train_model = pickle.load(pkl)


def predict(gender, married, dependent, education, self_employed, applicant_income,
            coApplicantIncome, loanAmount, loan_amount_term, creditHistory, propertyArea, feature_names=None):
    # Processing the input
    gen = 0 if gender == 'Male' else 1
    mar = 0 if married == 'Yes' else 1
    dep = float(0 if dependent == 'None' else 1 if dependent == 'One' else 2 if dependent == 'Two' else 3)
    edu = 0 if education == 'Graduate' else 1
    sem = 0 if self_employed == 'Yes' else 1
    pro = 0 if propertyArea == 'Semiurban' else 1 if propertyArea == 'Urban' else 2
    Lam = loanAmount / 1000
    cap = coApplicantIncome / 1000

    # Make prediction
    prediction = train_model.predict([[gen, mar, dep, edu, sem, applicant_income, cap,
                                       Lam, loan_amount_term, creditHistory, pro]])

    verdict = 'NOT ELIGIBLE' if prediction == 0 else 'ELIGIBLE'
    return verdict


if __name__ == '__main__':
    main()

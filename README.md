
# Loan Eligibility Prediction App

This is a Streamlit app that predicts whether an applicant is eligible for a loan based on various factors such as age, income, and credit history. The app is built using Python and scikit-learn, and uses a logistic regression model to make the prediction.

## Demo

You can try out a demo of the app here: https://paul0426-psm-loan-eligibility-prediction-loan-lg13sb.streamlit.app/

## Installation

To run the app locally, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/Paul0426/PSM_Loan_Eligibility_Prediction.git
   ```

2. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

3. Run the app:

   ```
   streamlit run loan.py
   ```

4. Open your web browser and go to http://localhost:8501 to view the app.

## Usage

To use the app, simply enter the required information in the input fields and click the "Predict" button. The app will then display the prediction, along with the probability of the applicant being eligible for a loan.

## Data

The app uses a dataset of loan applications that is included in the repository (`LoanApprovalPrediction.csv`). The dataset contains information about the applicants, such as their age, income, and credit history, as well as whether they were approved for a loan or not.

## Model

The app uses a Logistic Regression model to make the prediction. The model was trained using the loan application dataset and achieves an accuracy of 85%.

## Credits

This app was created by CB20025 PAUL LAW LIK PAO. If you have any questions or comments, feel free to contact me at CB20025@student.ump.edu.my .

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
# Loan Qualifier

This application prompts the user to collect the required information (credit scroe, monthly income, etc.), in order to create to a list of of loans that qualify for the user based on the amount they are looking for as well as the information collected. Then the user can choose whether or not to save the list of qualifying loans to a csv file of their choosing. 

---

## Technologies

Python 3.7.10 

Python Fire

Python Questionary

Python CSV Library

Python PyTest

## Installation Guide

Run these commands in the terminal to install the required libraries before runnning the application:

'''

    pip install fire

'''
    
    pip install questionary

'''

    pip install pytest

Run this command to start the application in the directory where the code is located:

'''
    
    python app.py

---

## Usage

Once you run 'python app.py' the project will run this function:

'''
   
    bank_data = load_bank_data()

    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )
    save_qualifying_loans(qualifying_loans)


In which it will ask the user to specify the daily rate sheet for the data. Then it will prompt the user to enter their credit score, current monthly debt, monthly income, desired loan amount, and home value.

![Loan-Qualifier-Example](Loan-Qualifier-Example.jpg)


The application then uses some calculations such as the debt-to-income ratio, the loan-to-value-ratio, etc. in order to find the qualifying loans and filter them into a list.

The user is then asked to confirm if they would like to save the list to a csv file of their choosing. The application then saves the file and exits. 

To run the tests and make sure the app is running correctly and saving loans run this command in the terminal:

'''

    pytest

---

## License

MIT License

Copyright (c) 2021 Talib Kateeb

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains helper functions for loading and saving CSV files.

"""
import csv
import questionary
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(csvpath, qualifying_loans):
    """Saves the list of qualifying loans to the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.
        qualifying_loans (list of lists): The qualifying bank loans.

    """
    
    #create header for the csv file

    header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]

    #Write the list of qualifying loans to the file
    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        for loan in qualifying_loans:
            csvwriter.writerow(loan)

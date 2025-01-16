import pandas as pd
from loan_service.models import UserTransactionInformation
from datetime import datetime

def import_csv_to_db(file_path):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Rename CSV columns to match Django model fields
    df = df.rename(columns={
        "user": "aadhar_id",
        "date": "registration_date",
        "transaction": "transaction_type",
        "amount": "amount",
    })

    # Convert the 'date' column to Django-compatible datetime format
    df["registration_date"] = pd.to_datetime(df["registration_date"], format="%Y-%m-%d")

    # Bulk create database entries
    transactions = [
        UserTransactionInformation(
            aadhar_id=row["aadhar_id"],
            registration_date=row["registration_date"],
            amount=row["amount"],
            transaction_type=row["transaction_type"].upper(),  # Ensure the type matches choices
        )
        for _, row in df.iterrows()
    ]

    # Save all objects to the database in one query
    UserTransactionInformation.objects.bulk_create(transactions)
    print(f"Imported {len(transactions)} records successfully!")

# Call the function with your CSV file
import_csv_to_db("transactions_data_backend__1_.csv")

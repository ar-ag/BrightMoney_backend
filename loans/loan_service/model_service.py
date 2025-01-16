from dateutil.relativedelta import relativedelta
from django.db.models import Sum
from loan_service.models import (UserInformation, UserTransactionInformation)

class UserInformationDbService:

    def __init__(self):
        self.user_information = UserInformation

    def get_user_by_uuid(self, user_uuid):
        return self.user_information.objects.filter(user_uuid=user_uuid).first()
    
    def create_user(self, name, email_id, annual_income, aadhar_id):
        return self.user_information.objects.create(
            name=name, email=email_id, annual_income=annual_income, aadhar_id=aadhar_id
        )
    
    def get_user_by_aadhar(self, aadhar_id):
        return self.user_information.objects.filter(aadhar_id=aadhar_id).first()
    
    def save_credit_score(self, aadhar_id, credit_score):
        self.user_information.objects.filter(aadhar_id=aadhar_id).update(credit_score=credit_score)

class UserTransactionInformationDbService:

    def __init__(self):
        self.user_transaction_information = UserTransactionInformation
    
    def is_user_transaction_exist(self, aadhar_id):
        return self.user_transaction_information.objects.filter(aadhar_id=aadhar_id).exists()

    def get_transactions_sum(self, aadhar_id, transaction_type):
        return self.user_transaction_information.objects.filter(
            aadhar_id=aadhar_id, transaction_type=transaction_type.upper()
        ).aggregate(total_amount=Sum("amount"))



# from ..model_service import UserInformationDbService, UserTransactionInformationDbService
# from ..tasks import calculate_credit_score

# class UserRegistrationService:
#     def __init__(self):
#         self.user_information_db_service = UserInformationDbService()
#         self.user_transaction_db_service = UserTransactionInformationDbService()

#     def register_user(self, payload):
#         print("hello from register user")
#         aadhar_id = payload.get("aadhar_id")
#         name = payload.get("name")
#         email_id = payload.get("email_id")
#         annual_income = payload.get("annual_income")

#         is_user_exist = self.user_information_db_service.get_user_by_aadhar(aadhar_id)
#         if is_user_exist:
#             return {'message': 'User already exists'}
        
#         is_user_transaction_exist = self.user_transaction_db_service.is_user_transaction_exist(aadhar_id)
#         if not is_user_transaction_exist:
#             return {
#                 'message': 'no user transactions found therefore cannot be registered'
#             }
#         user = self.user_information_db_service.create_user(name, email_id, annual_income, aadhar_id)

#         calculate_credit_score.delay(user.aadhar_id)
       
#         response = {
#                     'message': 'user successfully registered',
#                     'data': {
#                         'user_uuid': str(user.user_uuid)
#                     }}
        
#         return response
        

from ..model_service import UserInformationDbService, UserTransactionInformationDbService
from ..tasks import calculate_credit_score


class UserRegistrationService:
    def __init__(self):
        self.user_information_db_service = UserInformationDbService()
        self.user_transaction_db_service = UserTransactionInformationDbService()

    def register_user(self, payload):
        print("hello from register user")
        
        # Extract payload fields
        aadhar_id = payload.get("aadhar_id")
        name = payload.get("name")
        email = payload.get("email")  # Corrected field name
        annual_income = payload.get("annual_income")

        # Check if user already exists
        is_user_exist = self.user_information_db_service.get_user_by_aadhar(aadhar_id)
        if is_user_exist:
            return {'message': 'User already exists'}

        # Check if user transactions exist
        is_user_transaction_exist = self.user_transaction_db_service.is_user_transaction_exist(aadhar_id)
        if not is_user_transaction_exist:
            return {
                'message': 'No user transactions found, therefore cannot be registered'
            }

        # Create user
        try:
            user = self.user_information_db_service.create_user(name, email, annual_income, aadhar_id)
        except Exception as e:
            return {'message': 'Failed to create user', 'error': str(e)}

        # Trigger asynchronous credit score calculation
        try:
            calculate_credit_score.delay(user.aadhar_id)
        except Exception as e:
            return {
                'message': 'User registered, but failed to queue credit score calculation',
                'data': {'user_uuid': str(user.user_uuid)},
                'error': str(e)
            }

        # Successful response
        response = {
            'message': 'User successfully registered',
            'data': {'user_uuid': str(user.user_uuid)}
        }
        return response

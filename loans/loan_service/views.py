# from django.shortcuts import render
# import json
# import uuid
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse

# from .services.userRegistrationService import UserRegistrationService

# app_name = "loan_service"


# def register_user(request):

#     if request.method == "POST":
#         payload = json.loads(request.body)
#         response = UserRegistrationService().register_user(payload)

#         response["success"] = "False" if not response.get("data") else "True"
#         return HttpResponse(
#             json.dumps(response), status=200, content_type="application/json"
#         )
#     return HttpResponse(status=401)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserInformationSerializer
from .services.userRegistrationService import UserRegistrationService


class RegisterUserView(APIView):
    """
    API endpoint to register a user.
    """
    def post(self, request):
        serializer = UserInformationSerializer(data=request.data)
        
        if serializer.is_valid():
            # Call the service to register the user
            payload = serializer.validated_data
            service = UserRegistrationService()
            response = service.register_user(payload)

            # Check if user registration was successful
            if response.get('message') == 'User successfully registered':
                return Response(response, status=status.HTTP_201_CREATED)

            # Handle other cases (e.g., user already exists or missing transactions)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        # Return validation errors if serializer is invalid
        return Response(
            {"success": "False", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

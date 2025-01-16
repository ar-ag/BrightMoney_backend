from rest_framework import serializers
from loan_service.models import UserInformation
from loan_service.models import UserTransactionInformation

class UserInformationSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(required=True)
    class Meta:
        model=UserInformation
        fields="__all__"

class UserTransactionInformationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=UserInformation
        fields="__all__"

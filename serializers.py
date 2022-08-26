from rest_framework import serializers
from attendence_app.models import Employee


class Employee_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    # def post_data(self,data):
    #     item = Employee(first_name=data.get('first_name'),
    #                     last_name=data.get('last_name'),
    #                     address=data.get('address'),
    #                     email=data.get('email'))
    #     item.save()
    #     print("Reached")


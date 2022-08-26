from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from attendence_app.models import Employee
from serializers import Employee_Serializer
from rest_framework import status
from rest_framework import serializers


# Create your views here.
@api_view(['GET'])
def getdata(request):
    employee=Employee.objects.all()
    serializer=Employee_Serializer(employee,many=True)
    # person={'name':'arun','age':28}
    return Response(serializer.data)


@api_view(['POST'])
def postdata(request):
    # obj = Employee_Serializer()
    # item = obj.post_data(data=request.data)
    #
    # return Response(item,status=status.HTTP_201_CREATED)
    item = Employee_Serializer(data=request.data)

    # validating for already existing data
    if Employee.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)




@api_view(['POST'])
def update_items(request, id):
    item = Employee.objects.get(id=id)
    data = Employee_Serializer(instance=item, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_items(request, id):
    item = get_object_or_404(Employee, id=id)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


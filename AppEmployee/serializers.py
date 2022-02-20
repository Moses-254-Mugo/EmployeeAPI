from rest_framework import serializers
from AppEmployee.models import Departments, Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields =('DepartmentId', 'DepartmentName')

    
class EmployeeSerializer(serializers. ModelSerialier):
    class Meta:
        model = Employees
        fields = '__all__'

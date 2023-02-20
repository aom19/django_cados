from .models import Advocate , Company
from rest_framework import serializers


class CompanyListSerializer(serializers.ModelSerializer):
    employee_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Company
        fields = '__all__'

    def get_employee_count(self, obj):
        count = obj.advocate_set.count()
        return count


class AdvocatesListSerializer(serializers.ModelSerializer):
    company = CompanyListSerializer(read_only=True)
    class Meta:
        model = Advocate
        fields = ["id",'username','bio','company']


class AdvocatesDetailSerializer(serializers.ModelSerializer):
    company = CompanyListSerializer(read_only=True)
    class Meta:
        model = Advocate
        fields = ['id','username','bio', "company"]






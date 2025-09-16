from rest_framework import serializers
from .models import Student  

class StudentSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # name = serializers.CharField()
    # email = serializers.EmailField()
    # contact = serializers.CharField()

    # def create(self, validated_data):
    #     return Student.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.id = validated_data.get('id', instance.id)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.contact = validated_data.get('contact', instance.contact)
    #     instance.save()
    #     return instance
    class Meta:
        model=Student
        fields='__all__'
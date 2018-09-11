from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Users

class UserSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = User
		fields = ('id', 'username', 'is_staff')
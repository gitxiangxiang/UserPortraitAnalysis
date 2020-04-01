from rest_framework_mongoengine import serializers
from . import PersonalAppeal


class PersonalAppealSerializer(serializers.DocumentSerializer):
    class Meta:
        exclude = ('id',)
        model = PersonalAppeal.PersonalAppeal
        # fields = '__all__'

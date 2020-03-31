from rest_framework_mongoengine import serializers
from . import PersonalAppeal_mongo


class PersonalAppealSerializer(serializers.DocumentSerializer):
    class Meta:
        exclude = ('id',)
        model = PersonalAppeal_mongo.PersonalAppeal
        # fields = '__all__'

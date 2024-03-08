from rest_framework.serializers import ModelSerializer
from . import models


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = models.Project
        fields = "__all__"
    

class AboutSerializer(ModelSerializer):
    class Meta:
        model = models.About
        fields = "__all__"
    
class ProgrammingLangSerializer(ModelSerializer):
    class Meta:
        model = models.ProgrammingLang
        fields = ["name", "id"]
    
class TeamMemberSerializer(ModelSerializer):
    programming_languages = ProgrammingLangSerializer(many=True, read_only=True)
    class Meta:
        model = models.TeamMember
        fields = "__all__"

class ContactSerializer(ModelSerializer):
    class Meta:
        model = models.Contact
        fields = "__all__"



    

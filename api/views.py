from rest_framework.views import APIView
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework import status
import requests
TOKEN = "6984651478:AAEGU3F1IGU4zWVQsy2II-GPRsl2JKke7_4"
ADMIN_ID = (5601872113, 2095960669)
TG_ENDPOINT = f"https://api.telegram.org/bot{TOKEN}/"
class ProjectTable(APIView):
    def get(self, request):
        queryset = models.Project.objects.all()
        serialized_obj = serializers.ProjectSerializer(queryset, many=True)
        return Response(serialized_obj.data)

class AboutTable(APIView):
    def get(self, request):
        queryset = models.About.objects.first()
        serialized_obj = serializers.AboutSerializer(queryset)
        return Response(serialized_obj.data)

class TeamMemberTable(APIView):
    def get(self, request):
        queryset = models.TeamMember.objects.all()
        serialized_obj = serializers.TeamMemberSerializer(queryset, many=True)
        return Response(serialized_obj.data)

class ContactPost(APIView):
    def post(self, request):
        data = request.data
        # print(data)
        serialized_obj = serializers.ContactSerializer(data=data)
        if serialized_obj.is_valid():
            full_name = data["full_name"]
            message = data["message"]
            email = data["email"]
            number =str(data["number"])
            for admin in ADMIN_ID:
                try:
                    tg = data["telegram_username"]
                    requests.get(f"{TG_ENDPOINT}sendMessage?chat_id={admin}&text=YangiSo'rov\nIsmi:{full_name}\nnumber: +998{number}\ntelegram username: {tg}\nEmail: {email}\nQoldirgan Xabar:\n{message}")
                except:
                    requests.get(f"{TG_ENDPOINT}sendMessage?chat_id={admin}&text=YangiSo'rov\nIsmi:{full_name}\nnumber: {number}\ntelegram username: Qoldirmadi\nEmail: {email}\nQoldirgan Xabar:\n{message}")    
            serialized_obj.save()
            return Response(201, status=status.HTTP_201_CREATED)
        return Response(serialized_obj.errors)
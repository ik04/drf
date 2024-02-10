from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PeopleSerializer,LoginSerializer,RegisterSerializer
from django.contrib.auth.models import User

@api_view(["GET","POST"])
def index(request):
    if request.method == "GET":
        return Response(data={"message":"hi mom"},status=status.HTTP_200_OK)
    
@api_view(["POST","GET","PATCH","DELETE"])
def store(request):
    if request.method == "GET":
        people = Person.objects.all()
        serializer = PeopleSerializer(people, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ["PATCH", "PUT"]:
        try:
            person = Person.objects.get(id=request.data.get("id"))
        except Person.DoesNotExist:
            return Response({"error": "Person not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PeopleSerializer(person, data=request.data, partial=request.method == "PATCH")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        try:
            person = Person.objects.get(id=request.data.get("id"))
        except Person.DoesNotExist:
            return Response({"error": "Person not found"}, status=status.HTTP_404_NOT_FOUND)

        person.delete()
        return Response({"message": "Person deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(["POST"])
def login(request):
    data = request.data
    serializer = LoginSerializer(data=data)
    if serializer.is_valid():
        data = serializer.validated_data
        return Response({"message":"success"})
   
class RegisterApi(APIView):
    def post(self,request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if not serializer.is_valid():
            return Response({"errors":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({"message":"user created"},status=status.HTTP_201_CREATED)

class LoginApi(APIView):
    def post(request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            data = serializer.validated_data
        return Response({"message":"success"})

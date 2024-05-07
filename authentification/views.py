from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class HomeView(APIView):
     
    permission_classes = (IsAuthenticated,)
    def get(self, request): 
        respuesta = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
        return Response(respuesta)

class LogoutView(APIView):
     permission_classes = (IsAuthenticated,)
     def post(self, request):          
          try:
               refresh_token = request.data["refresh_token"]
               token = RefreshToken(refresh_token)
               token.blacklist()
               return Response(status=response.status.HTTP_205_RESET_CONTENT)
          except Exception as e:
               return Response(status=response.status.HTTP_400_BAD_REQUEST)
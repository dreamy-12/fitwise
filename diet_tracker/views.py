from django.shortcuts import render

from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication,permissions
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView


from diet_tracker.models import FoodLog
from diet_tracker.serializers import FoodLogSerializer
# Create your views here.


class FoodLogListCreateView(ListAPIView,CreateAPIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=FoodLogSerializer
    queryset=FoodLog.objects.all()

    # def get(self,request):

    #     instance=FoodLog.objects.all()

    #     serializer_instance=FoodLogSerializer(instance, many=True)

    #     return Response(serializer_instance.data,status=status.HTTP_200_OK)

    # def post(self,request):

    #     form_data=request.data

    #     serializer_instance=FoodLogSerializer(data=form_data)

    #     if serializer_instance.is_valid():

    #         serializer_instance.save()

    #         return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
    #     else:

    #         return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

# from django.shortcuts import get_object_or_404

class FoodLogRetrieveUpdateDelete(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    serializer_class=FoodLogSerializer

    queryset= FoodLog.objects.all()

    # def get(self,request,pk=None):

    #     instance=get_object_or_404(FoodLog,id=pk)

    #     serializer_instance=FoodLogSerializer(instance)

    #     return Response(serializer_instance.data,status=status.HTTP_200_OK)

    # def put(self,request,pk=None):

        
    #     instance= get_object_or_404(FoodLog,id=pk)

    #     form_data=request.data    
    
    #     serializer_instance=FoodLogSerializer(data=form_data,instance=instance)
    
    #     if serializer_instance.is_valid():
    
    #         serializer_instance.save()
        
    #         return Response(form_data,status=status.HTTP_200_OK)
    
    #     else:
    
    #         return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)        

    # def delete(self,request,pk=None):

    #     instance=get_object_or_404(FoodLog,id=pk)# to check that instance is present-particular\ one object

    #     instance.delete()
        
    #     return Response({"message":"Deleted..!"},status=status.HTTP_200_OK)

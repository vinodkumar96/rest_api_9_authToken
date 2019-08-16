from django.shortcuts import render
from .serializers import ProductSerializer
from .models import Product
from rest_framework import generics
from .permissions import IsAdminorReadOnly
#
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.http import HttpResponse

# Create your views here.
def input(request):
    return render(request,'input.html')
def link(request):
    p_id1 = int(request.POST['t1'])
    p_name1 = request.POST['t2']
    p_cost1 = float(request.POST['t3'])
    p_mfd1 = request.POST['t4']
    p_exd1 = request.POST['t5']
    f =Product(p_id=p_id1,p_name=p_name1,p_cost=p_cost1,p_mfd=p_mfd1,p_exd=p_exd1)
    f.save()
    return render(request,'link.html')
def display(request):
    recs = Product.objects.all()
    return render(request,'display.html',{'recs':recs})

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminorReadOnly,)

class ProductList1(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminorReadOnly,)
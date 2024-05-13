from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Producto,Venta,DetalleVenta
from .serializer import ProductoSerializer,VentaSerializer, DetalleVentaSerializer


class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)
    
class ProductoView(APIView):
    
    def get(self,request):
        producto = Producto.objects.all()
        serProducto = ProductoSerializer(producto,many=True)
        return Response(serProducto.data)
    
    def post(self,request):
        serProducto= ProductoSerializer(data=request.data)
        serProducto.is_valid(raise_exception=True)
        serProducto.save()
        
        return Response(serProducto.data)
    
class ProductoDetalleView(APIView):
    
    def get(self,request,producto_id):
        producto= Producto.objects.get(pk=producto_id)
        serProducto= ProductoSerializer(producto)
        return Response(serProducto.data)
    
    def put(self,request,producto_id):
        producto= Producto.objects.get(pk=producto_id)
        serProducto= ProductoSerializer(producto,data=request.data)
        serProducto.is_valid(raise_exception=True)
        serProducto.save()
        return Response(serProducto.data)
    
    def delete(self,request,producto_id):
        producto= Producto.objects.get(pk=producto_id)
        serProducto= ProductoSerializer(producto)
        producto.delete()
        return Response(serProducto.data)

class VentaView(APIView):
    def get(self,request):
        venta = Venta.objects.all()
        serVenta = VentaSerializer(venta,many=True)
        return Response(serVenta.data)

    def post(self,request):
        serVenta = VentaSerializer(data=request.data)
        serVenta.is_valid(raise_exception=True)
        serVenta.save()

class VentaDetalleView(APIView):
    def get (self,request,venta_id):
        venta = Venta.objects.get()
        serVenta = VentaSerializer(venta)
        return Response(serVenta.data)
    
    def put(self,request,venta_id):
        venta = Venta.objects.get(pk=venta_id)
        serVenta = VentaSerializer(venta,data=request.data)
        serVenta.is_valid(raise_exception=True)
        serVenta.save()
        return Response(serVeta.data)
    
    def delete(self,request,venta_id):
        venta = Venta.objects.get(pk=venta_id)
        serVenta = VentaSerializer(venta)
        venta.delete()
        return Response(serVenta.data)
    
class DetalleVentaView(APIView):
    def get(self,request):
        detalleVenta = DetalleVenta.objects.all()
        serDetalleVenta = DetalleVentaSerializer(detalleVenta,many=True)
        return Response (serDetalleVenta.data)
    
    def post(self,request):
        serDetalleVenta = DetalleVentaSerializer(data=request.data)
        serDetalleVenta.is_valid(raise_exception=True)
        serDetalleVenta.save()

class DetalleVentaDetalleView(APIView):
    def get(self,request,venta_id,producto_id):
        detalleVenta = DetalleVenta.objects.get()
        serDetalleVenta = DetalleVentaSerializer(detalleVenta)
        return Response(serDetalleVenta.data)
    
    def put(self,request,venta_id,producto_id):
        detalleVenta = DetalleVenta.objects.get(producto=producto_id, venta = venta_id)
        serDetalleVenta = DetalleVentaSerializer(detalleVenta,data=request.data)
        serDetalleVenta.is_valid(raise_exception = True)
        serDetalleVenta.save()
        return Response(serDetalleVenta.data)
    
    def delete(self,request,venta_id,producto_id):
        detalleVenta = DetalleVenta.objects.get(producto=producto_id, venta = venta_id)
        serDetalleVeta = DetalleVentaSerializer(detalleVenta)
        detalleVenta.delete()
        return Response(serDetalleVenta.data)
        
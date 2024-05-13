from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    #PRODUCTO
    path('producto',views.ProductoView.as_view(),name='serializer.producto'),
    path('producto/<int:producto_id>',views.ProductoDetalleView.as_view()),
    #VENTA
    path('venta',views.VentaView.as_view(),name='serializer.venta'),
    path('venta/<int:venta_id>',views.VentaDetalleView.as_view()),
    #DETALLEVENTA
    path('detalle_venta',views.DetalleVentaView.as_view(),name='serializer.detalle_venta'),
    path('detalle_venta/<int:venta_id>/<int:producto_id>',views.DetalleVentaDetalleView.as_view()),
]
from django.shortcuts import render
from django.views.generic import ListView

from .models import Producto


def inicio(request):
    total_productos = Producto.objects.filter(disponible=True).count()

    return render(
        request,
        "catalogo/inicio.html",
        {"total_productos": total_productos},
    )


class ProductoListView(ListView):
    model = Producto
    template_name = "catalogo/producto_list.html"
    context_object_name = "productos"
    queryset = Producto.objects.filter(disponible=True).order_by("-id")
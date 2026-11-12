from django.urls import path

from . import views


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("productos/", views.ProductoListView.as_view(), name="lista_productos"),
]
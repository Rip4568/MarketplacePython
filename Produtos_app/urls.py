
from django.urls import path
from . import views

app_name = "Produtos_app"#Produtos_app  

urlpatterns = [
    path('',views.ProductListView.as_view(),name='list'),
    path("<slug:slug>/", views.ProductDetailView.as_view(), name="detail"),
    path("category/<slug:slug>/", views.ProductListView.as_view(), name="list_by_category"),
    
]
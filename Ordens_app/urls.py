from django.urls import path

from .views import OrderCreateView

app_name = 'Ordens_app'

urlpatterns = [
    path('create',OrderCreateView.as_view(),name='ordercreateview')
]

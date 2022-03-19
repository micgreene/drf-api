from django.urls import path
from .views import FruitList, FruitDetail

urlpatterns =[
    path('', FruitList.as_view(), name='fruit_list'),
    path('<int:pk>/', FruitDetail.as_view(), name='fruit_detail'),
]
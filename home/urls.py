from django.urls import path ,include
from . import views


urlpatterns = [
    path('list',views.list, name='list_data'),
    path('filter_list/',views.filter_list, name='filter_list_data'),
]
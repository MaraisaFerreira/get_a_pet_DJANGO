from django.urls import path
from . import views

app_name = 'pets'

urlpatterns = [
    path('', views.home, name='home'),
    path('pet/<int:pet_id>', views.pet_details, name='pet_detail'),

]

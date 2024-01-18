from django.urls import path
from . import views

app_name = 'pets'

urlpatterns = [
    # pets
    path('pets/', views.home, name='home'),
    path('pet/<int:pet_id>', views.pet_details, name='pet_detail'),
    path('pet/add', views.add_pet, name='add_pet'),

    # user
    path('register/', views.register_user, name='register')
]

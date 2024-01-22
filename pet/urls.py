from django.urls import path
from . import views

app_name = 'pets'

urlpatterns = [
    # pets
    path('pets/', views.home, name='home'),
    path('pet/<int:pet_id>/', views.pet_details, name='pet_detail'),
    path('pet/add/', views.add_pet, name='add_pet'),
    path('pet/edit/<int:pet_id>/', views.edit_pet, name='edit_pet'),
    path('pet/delete/<int:pet_id>/', views.delete_pet, name='delete_pet'),
    path('pets/my_pets/', views.my_pets, name='my_pets'),

    # user
    path('register/', views.register_user, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]

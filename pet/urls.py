from django.urls import path
from . import views

app_name = 'pets'

urlpatterns = [
    # pets
    path('pets/', views.home, name='home'),
    path('pet/<int:pet_id>', views.pet_details, name='pet_detail'),

    # user
    path('register/', views.register_user, name='register')
]

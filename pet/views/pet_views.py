from django.shortcuts import render
from pet.models import Pet


def home(request):
    pets_list = Pet.objects.all()
    print(pets_list)

    return render(
        request,
        'pet/home.html',
        {
            'doc_title': 'Pets',
            'pets': pets_list
        }
    )

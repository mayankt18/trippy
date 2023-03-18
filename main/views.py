from django.shortcuts import render
from .models import Sponsor

# Create your views here.
def index(request):
    return render(request, 'base.html')





def sponsor_list(request):
    sponsors_by_type = {}
    for choice in Sponsor.TYPE_CHOICES:
        sponsors_by_type[choice[1]] = Sponsor.objects.filter(type=choice[0])
    context = {'sponsors_by_type': sponsors_by_type}
    return render(request, 'sponsor_list.html', context)

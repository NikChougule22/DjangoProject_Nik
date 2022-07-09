from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    
    # dest1= Destination()
    # dest1.name='Mumbai'
    # dest1.desc='The City that Never Sleeps'
    # dest1.img='destination_1.jpg'
    # dest1.price=700
    # dest1.offer=True
    
    # dest2= Destination()
    # dest2.name='Hyderabad'
    # dest2.desc='The City of Biryani'
    # dest2.img='destination_2.jpg'
    # dest2.price=600
    # dest2.offer=True
    
    # dest3= Destination()
    # dest3.name='Bengluru'
    # dest3.desc='The City of Gardens'
    # dest3.img='destination_3.jpg'
    # dest3.price=1000
    # dest3.offer=False
    
    # dests=[dest1, dest2, dest3]
    
    dests=Destination.objects.all()
    
    return render(request,"index.html",{'dests':dests} )
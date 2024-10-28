from django.shortcuts import render
from django.http import HttpResponse
from .models import Makanan,Kantin
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):

    # ngambil objek orm
    kantins = Kantin.objects.all()

    # requset 
    searchMakanan = request.GET.get('nama')
    searchKantin = request.GET.get('kantin_id')


    if searchMakanan:
        makanans = Makanan.objects.filter(nama__icontains=searchMakanan)
    elif searchKantin:
        makanans = Makanan.objects.filter(kantin = searchKantin)
    else:
        makanans = Makanan.objects.all()

    return render(request, 'home.html', {
        'searchMakanan':searchMakanan,
        'makanans' : makanans,
        'kantins' : kantins,
        'page' : 'about'
        })
    
def detail(request,makanan_id):
    makanan = get_object_or_404(Makanan,pk=makanan_id)
    return render(request,'detail.html',{
        'makanan' : makanan,
        'page' : 'about',
        'ketersediaan' : makanan
        })

def about(request):
    return render(request,'about.html', { 'page' : 'about' })
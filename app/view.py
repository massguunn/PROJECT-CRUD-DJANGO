from django.http import HttpResponse

def home(request):
    return HttpResponse("Selamat datang di halaman utama!")

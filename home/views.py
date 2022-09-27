from django.shortcuts import render, HttpResponse
from .models import Certificate
from Courses.config import generate_slug

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def cert_check(request, slug):
    try:
        std = Certificate.objects.filter(slug = slug)[0]
        return render(request, 'cert.html', {'std':std})
    except:
        std = {
            "student_name" : "No certificate found",
            "student_id" : "None",
            "cert_number" : None,
            "cert_created" : "Certificate ID is invalid",
            "course" : "-",
            "slug" : "nocertificate",
            "gdrive_id" : "1O0EVKgJOKO_Y4MYlz_eKuufdbcSKFsO7",
        }
        return render(request, 'cert.html', {'std':std})


def search_cert(request):
    query = request.GET['cert_id']
    return cert_check(request=request,slug=generate_slug(query))
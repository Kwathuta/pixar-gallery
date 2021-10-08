from django.shortcuts import render
from .models import Image
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse

# Create your views here.


def gallery(request):
    try:
        images = Image.objects.all()
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'gallery.html', {'image': images})

from django.shortcuts import render
from .models import Image
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse

# Create your views here.


def gallery(request):
    categories = Image.objects.distinct().values_list('category__name', flat=True)
    try:
        images = Image.objects.all()
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'gallery.html', {'image': images, 'categories': categories})


def search_images(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched_images = Image.search_by_name(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'message': message, 'images': searched_images})
    else:
        message = "You haven't searched for any search term"
        return render(request, 'search.html', {'message': message})


def view_category(request, category):
    categories = Image.objects.distinct().values_list('category__name', flat=True)
    image = Image.objects.filter(category__name=category)
    return render(request, 'category.html', {"image": image, 'categories': categories})

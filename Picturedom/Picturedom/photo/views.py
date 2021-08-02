from django.shortcuts import render

from Picturedom.photo.models import Photo


def homepage_photos(request):
    """
    Shows all the photos on the homepage, ordered by the most recent posted one
    """
    photos = Photo.objects.all().order_by('-posted_at')
    context = {
        'photos': photos
    }
    return render(request, 'photos/homepage_photos.html', context)

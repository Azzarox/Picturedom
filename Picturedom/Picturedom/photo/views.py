from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Picturedom.photo.forms import PhotoForm
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


@login_required()
def create_photo(request):
    """
    Creates new photo. Automatically assigns the 'posted_by' property to the user.
    """
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.posted_by = request.user
            photo.save()
            return redirect('homepage photos')
    else:
        form = PhotoForm()

    context = {
        'form': form
    }
    return render(request, 'photos/create_photo.html', context)

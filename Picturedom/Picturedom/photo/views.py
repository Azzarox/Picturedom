from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Picturedom.photo.forms import PhotoForm, PhotoCommentForm
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


def photo_comments(request, pk):
    """
    Shows the 3 most recent comments.
    Shows the comment text box - GET.
    """
    photo = Photo.objects.get(pk=pk)
    comments = photo.comment_set.all().order_by('-posted_at')[:3]
    context = {
        'photo': photo,
        'comments': comments,
        'form': PhotoCommentForm(initial={
            'image_pk': pk
        }),
    }
    return render(request, 'photos/comments.html', context)


def add_comment(request, pk):
    """
    Adds comment to the image - POST.
    Checks the user and assigns it to the comment.posted_by
    """
    form = PhotoCommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()
    else:
        text = 'You have used forbidden word!'
        messages.warning(request, text)
    return redirect('photo comments', pk)

# edit comment only for the user logged in

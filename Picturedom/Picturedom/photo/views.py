from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from Picturedom.photo.forms import PhotoForm, PhotoCommentForm, EditCommentForm
from Picturedom.photo.models import Photo, Comment, CommentDislike, CommentLike, Category


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


@login_required()
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


@login_required
def edit_comment(request, pk):
    comment = Comment.objects.filter(user=request.user).get(pk=pk)
    image_pk = comment.comment_image.id
    if request.method == 'POST':
        form = EditCommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('photo comments', image_pk)
    else:
        form = EditCommentForm(instance=comment)

    context = {
        'form': form,
        'comment': comment,
    }
    return render(request, 'photos/edit_comment.html', context)


@login_required
def delete_comment(request, pk):
    comment = Comment.objects.filter(user=request.user).get(pk=pk)
    image_pk = comment.comment_image.id
    comment.delete()
    return redirect('photo comments', image_pk)


@login_required()
def like_comment(request, pk):
    """
    Likes the given comment, if already liked by the user it sends message and doesn't POST.
    """
    comment = Comment.objects.get(pk=pk)
    photo_pk = comment.comment_image.id
    # checks if there is a like by the user
    is_liked_by_user = comment.commentlike_set.filter(
        user=request.user).exists()

    if not is_liked_by_user:
        likes = CommentLike(
            comment=comment,
            user=request.user
        )
        likes.save()
    else:
        messages.warning(request, 'You have already liked this comment')

    return redirect('photo comments', photo_pk)


@login_required()
def dislike_comment(request, pk):
    """
    Dislikes the given comment, if already disliked by the user it sends message and doesn't POST.
    """
    comment = Comment.objects.get(pk=pk)
    photo_pk = comment.comment_image.id
    # checks if there is a dislike by the user
    is_disliked_by_user = comment.commentdislike_set.filter(
        user=request.user).exists()

    if not is_disliked_by_user:
        dislikes = CommentDislike(
            comment=comment,
            user=request.user
        )
        dislikes.save()
    else:
        messages.warning(request, 'You have already disliked this comment')
    return redirect('photo comments', photo_pk)


@login_required()
def user_photos(request):
    user_pictures = request.user.photo_set.all()

    context = {
        'user_photos': user_pictures,
    }
    return render(request, 'photos/user_photos.html', context)


def photo_category(request, pk):
    """
    Takes all images that are in the category chosen and shows only 6 of them per page.
    """
    category = Category.objects.get(pk=pk)
    photos = category.photo_set.all()

    paginator = Paginator(photos, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'photos': photos,
        'page_obj': page_obj,
    }
    return render(request, 'photos/photo_category.html', context)

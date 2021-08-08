from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Picturedom.profile_user.forms import ProfileForm, DeleteProfileImageForm
from Picturedom.profile_user.models import Profile


@login_required
def profile_details(request):
    """
    Mainly edits user profile fields.
    Displays total user photos, comments, likes.
    """
    profile = Profile.objects.get(user_id=request.user.id)
    profile.full_name = profile.first_name + ' ' + profile.last_name
    user_images = request.user.photo_set.count()
    user_comments = request.user.comment_set.count()
    user_liked = request.user.commentlike_set.count()
    all_likes_from_images = sum([photo.photolike_set.count() for photo in request.user.photo_set.all()])

    # Shows latest 4 pictures
    recent_photos = request.user.photo_set.all().order_by('-posted_at')[:4]
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        delete_image_form = DeleteProfileImageForm(request.POST)
        if form.is_valid() and delete_image_form.is_valid():
            profile = form.save(commit=False)
            if delete_image_form.cleaned_data['delete_image'] == 'True':
                profile.image.delete()
            else:
                profile.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
        delete_image_form = DeleteProfileImageForm()

    context = {
        'form': form,
        'delete_image_form': delete_image_form,
        'profile': profile,
        'user_images': user_images,
        'user_comments': user_comments,
        'user_liked': user_liked,
        'total_likes': all_likes_from_images,
        'recent_photos': recent_photos,
    }

    return render(request, 'profile/profile.html', context)

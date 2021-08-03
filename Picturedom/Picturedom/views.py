from django.core.exceptions import SuspiciousOperation, PermissionDenied
from django.http import Http404, HttpResponseServerError
from django.shortcuts import render


# Custom Handlers

def error_400_view(request, exception):
    return render(request, 'errors/400.html', status=400)


def error_403_view(request, exception):
    return render(request, 'errors/403.html', status=403)


def error_404_view(request, exception):
    return render(request, 'errors/404.html', status=404)


def error_500_view(request):
    return render(request, 'errors/500.html', status=500)


# Raising error

def raise_error_400_bad_request(request):
    raise SuspiciousOperation


def raise_error_403_forbidden(request):
    raise PermissionDenied


def raise_error_404_page_not_found(request):
    raise Http404('Exception')


def raise_error_500_server_error(request):
    raise HttpResponseServerError

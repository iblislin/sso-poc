from oauth2_provider.decorators import protected_resource

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'sso/index.html')


@protected_resource(scopes=['foo'])
def user(request):
    u = request.user
    print(request.user)

    return JsonResponse({  # format of phabricator
        'id': u.id,
        'username': u.username,
        'name': ' '.join((u.first_name, u.last_name)),
        'email': u.email,
        'link': '',
        'image': '',
    })

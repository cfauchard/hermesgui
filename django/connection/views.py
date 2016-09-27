from django.shortcuts import render

# Create your views here.

from .permissions import permission_test
from .models import Connection
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

@login_required
def detail(request, connection_name):
    connection_selected = (Connection.objects.get(name=connection_name))

    if permission_test(request, connection_selected) == False:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    context = {
        'connection': connection_selected,
    }
    return render(request, 'connection/detail.html', context)

@login_required
def index(request):
    latest_connection_list = Connection.objects.order_by('name')[:100]
    context = {'latest_connection_list': latest_connection_list}
    return render(request, 'connection/index.html', context)




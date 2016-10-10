from django.shortcuts import render

# Create your views here.

from .permissions import permission_test, get_authorized_connections
from .models import Connection
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required


from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from .forms import ConnectionForm

@login_required
def detail(request, connection_name):
    connection_selected = (Connection.objects.get(name=connection_name))

    if permission_test(request, connection_selected) == False:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    connection_selected = get_object_or_404(Connection, pk=connection_name)

    if request.method == 'POST':
        form = ConnectionForm(request.POST, instance = connection_selected)
        if form.is_valid():
            connection_selected = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            connection_selected.save()
            return HttpResponseRedirect('/connection')
    else:
        form = ConnectionForm(instance = connection_selected)
        return render(request, 'connection/detail.html', {'form': form})

@login_required
def index(request):
    connection_list = get_authorized_connections(request)
    connection_list_size = len(connection_list)
    context = {
        'connection_list': connection_list,
        'connection_list_size': connection_list_size,
        'max_rows': settings.MAX_ROWS,
    }
    return render(request, 'connection/index.html', context)

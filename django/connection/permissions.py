from .models import Permission
from django.conf import settings
from .models import Connection

def permission_test(request, connection):
    if not request.user.is_superuser:
        groups = request.user.groups.all()
        if Permission.objects.filter(connection=connection.name).filter(group__in=groups).count() == 0:
            return False

    return True

def get_authorized_connections(request):
    if request.user.is_superuser:
        connection_list = Connection.objects.order_by('name')[:settings.MAX_ROWS]

    else:
        groups = request.user.groups.all()

        connection_list = Connection.objects.filter(group__in=groups).order_by('name')[:settings.MAX_ROWS]
        #connection_list = Connection.objects.order_by('name')[:settings.MAX_ROWS]

    return connection_list
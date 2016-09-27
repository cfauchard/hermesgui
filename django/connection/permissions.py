from .models import Permission

def permission_test(request, connection):
    if not request.user.is_superuser:
        groups = request.user.groups.all()
        if Permission.objects.filter(connection=connection.name).filter(group__in=groups).count() == 0:
            return False

    return True
from django.db import models

# Create your models here.

class Connection(models.Model):
    GET = 'get'
    PUT = 'put'
    COMMANDS = (
        (GET, 'GET'),
        (PUT, 'PUT'),
    )

    SFTP = 'sftp'
    FTP = 'ftp'
    PROTOCOLS = (
        (SFTP, 'SFTP'),
        (FTP, 'FTP'),
    )

    name = models.CharField(max_length=80, blank=False, default="", primary_key=True, unique=True)
    host = models.CharField(max_length=80, blank=False, default="localhost")
    protocol = models.CharField(
        max_length=4,
        choices=PROTOCOLS,
        default=SFTP,
    )
    user = models.CharField(max_length=30, blank=False, default="")
    password = models.CharField(max_length=30, default="", blank=True)
    private_key = models.CharField(max_length=80, blank=True, default="")
    deleteflag = models.BooleanField(default=None)
    activation = models.BooleanField(default=None)
    command = models.CharField(
        max_length=3,
        choices=COMMANDS,
        default=GET,
    )
    excluderegex = models.CharField(max_length=30, default="", blank=True)
    includeregex = models.CharField(max_length=30, default="", blank=True)
    localdir = models.CharField(max_length=80, blank=False, default="")
    statuslogdir = models.CharField(max_length=80, blank=True, default="")
    backupdir = models.CharField(max_length=80, blank=True, default="")
    remotedir = models.CharField(max_length=80, blank=True, default="")
    logfile = models.CharField(max_length=80, blank=True, default="")
    group = models.CharField(max_length=80, blank=True, default="")

    def __str__(self):
        return self.name


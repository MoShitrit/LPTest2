from __future__ import unicode_literals

from django.db import models


class Version(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name


class Lob(models.Model):
    name = models.CharField(max_length=10, unique=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return '{0}  [{1}]'.format(self.name, self.location)


class Site(models.Model):
    id = models.CharField(primary_key=True, max_length=20, unique=True)
    lob = models.ForeignKey(Lob, on_delete=models.CASCADE)
    version = models.ForeignKey(Version, on_delete=models.CASCADE)
    comments = models.CharField(max_length=100, blank=True)
    date_added = models.DateTimeField('date_added', auto_now_add=True)

    def __str__(self):
        if self.comments:
            return '{0} - {1}, {2} ({3})'.format(self.id, self.lob, self.version, self.comments)
        else:
            return '{0} - {1}, {2}'.format(self.id, self.lob, self.version)

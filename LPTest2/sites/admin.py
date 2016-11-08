from django.contrib import admin

from .models import Site, Lob, Version

admin.site.register(Site)
admin.site.register(Lob)
admin.site.register(Version)


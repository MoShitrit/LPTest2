from django.shortcuts import render
from time import strftime
from .models import Lob, Site, Version
from .forms import SiteForm


def home(request):
    return render(request, "home.html", {'date': strftime("%A, %B %d %Y"),
                                         'lobs': Lob.objects.all(),
                                         'sites': Site.objects.all(),
                                         'versions': Version.objects.all(),
                                         'show_add_site': True})


def site(request, lob, site_id):
    site_arg = Site.objects.filter(id=site_id)
    if str(site_arg.first().lob.name) == 'ALPHA':
        return render(request, "site_ALPHA.html",
                      {'date': strftime("%A, %B %d %Y"),
                       'site': site_id,
                       'title': '{0} {1} Site - {2}'.format(lob, 'ALPHA', site_id),
                       'lobs': Lob.objects.all(),
                       'sites': Site.objects.all(),
                       'versions': Version.objects.all(),
                       'show_add_site': True})

    version = str(site_arg.first().version)
    return render(request, "site_%s.html" % version,
                  {'date': strftime("%A, %B %d %Y"),
                   'site': site_id,
                   'title': '{0} {1} Site - {2}'.format(lob, version, site_id),
                   'lobs': Lob.objects.all(),
                   'sites': Site.objects.all(),
                   'versions': Version.objects.all(),
                   'show_add_site': True})


def add_site(request):
    if request.method == 'POST':
        form = SiteForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "site_added.html", {'show_add_site': False})
    else:
        form = SiteForm()
        return render(request, "add_site.html", {'form': form})


def site_added(request):
    return render(request, "site_added.html", {'show_add_site': True})


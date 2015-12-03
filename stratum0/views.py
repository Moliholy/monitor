from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import never_cache, cache_page
from django.conf import settings

from stratum0.models import Stratum0, Stratum1, ReplicationSite

def index(request):
    stratum0s = Stratum0.objects.all()
    context = { 'stratum0s': stratum0s }
    return render(request, 'stratum0/index.html', context)


@never_cache
def details(request, stratum0_fqrn):
    stratum0  = get_object_or_404(Stratum0, fqrn=stratum0_fqrn)
    stratum1s = Stratum1.objects.filter(stratum0=stratum0)
    browser_url = ''
    if settings.MONITOR_SHOW_BROWSER_URL:
        pos = request.path[:-1].rfind('/')
        browser_url = '/'.join(
            [request.path[0:pos], 'cb/browser', stratum0.fqrn, 'latest'])

    context   = { 'stratum0'    : stratum0,
                  'stratum1s'   : stratum1s,
                  'browser_url' : browser_url
                  }
    return render(request, 'stratum0/details.html', context)


@cache_page(60)
def stratum0_details(request, stratum0_fqrn):
    stratum0 = get_object_or_404(Stratum0, fqrn=stratum0_fqrn)
    stratum1s = Stratum1.objects.filter(stratum0=stratum0)
    context  = { 'stratum0' : stratum0,
                 'stratum1s' : stratum1s }
    return render(request, 'stratum0/stratum0_details.json', context,
                  content_type="application/json")


@cache_page(60)
def stratum1_details(request, stratum0_fqrn, stratum1_id):
    stratum0 = get_object_or_404(Stratum0, fqrn=stratum0_fqrn)
    stratum1 = get_object_or_404(Stratum1, pk=stratum1_id, stratum0=stratum0)
    context = { 'stratum0'     : stratum0,
                'stratum1'     : stratum1 }
    return render(request, 'stratum0/stratum1_details.json', context,
                  content_type="application/json")


@never_cache
def matrix(request):
    replication_sites = ReplicationSite.objects.all().order_by('name')
    stratum0s         = Stratum0.objects.all().order_by('name')
    s_map = []

    # TODO: fix that crap!
    for stratum0 in stratum0s:
        stratum1s = []
        for repl_site in replication_sites:
            try:
                stratum1 = Stratum1.objects.get(stratum0=stratum0,
                                                replication_site=repl_site)
                stratum1s.append(stratum1)
            except Exception, e:
                stratum1s.append(None)
        s_map.append((stratum0, stratum1s))

    context = { 'replication_sites' : replication_sites,
                'stratum1_map'      : s_map }
    return render(request, 'stratum0/matrix.html', context)

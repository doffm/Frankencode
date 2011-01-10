from frankfeeds.models import Snippet

def this_site (request):
    try:
        this_site = Snippet.objects.get(name='this-site')
    except:
        this_site = ''
    return {'this_site':this_site}

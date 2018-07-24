
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse

from .models import Link
from .forms import LinkForm

from .req_to_1c import Req


def index(request):

    links = Link.objects.order_by('date_added')
    context = {'links': links}

    return render(request, 'audit/index.html', context)


def new_link(request):

    if request.method != 'POST':
        form = LinkForm()
    else:
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.save()

            link_id = link.id
            text = request.POST['text']

            req = Req(link_id, text)
            req.req_to_1c()

            return HttpResponseRedirect(reverse('audit:index'))
    context = {'form': form}
    return render(request, 'audit/new_link.html', context)


@csrf_exempt
def new_link_1c(request):

    if request.method == 'POST':
        link_id = int(request.POST['link_id'])
        check = request.POST['check']

        link = Link.objects.get(id=link_id)
        link.check = check
        link.save()

        return JsonResponse({'status': 'ok'})

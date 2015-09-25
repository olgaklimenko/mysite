from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from photo_gallery.models import Item, Photo

class IndexView(generic.ListView):
    template_name = 'photo_gallery/index.html'
    context_object_name = 'latest_item_list'

    def get_queryset(self):
        return Item.objects.order_by('name')[:5]

class DetailView(generic.DetailView):
    model = Item
    template_name = 'photo_gallery/detail.html'
    
    def get_queryset(self):
        return Item.objects.all()

class ResultsView(generic.DetailView):
    model = Item
    template_name = 'photo_gallery/results.html'

def vote(request, item_id):
    p = get_object_or_404(Item, pk=item_id)
    try:
        selected_photo= p.photo_set.get(pk=request.POST['photo'])
    except (KeyError, Photo.DoesNotExist):
        return render(request, 'photo_gallery/detail.html', {
            'photo':p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_photo.votes +=1
        selected_photo.save()
        return HttpResponseRedirect(reverse('photo_gallery:results', args=(p.id,)))

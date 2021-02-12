from django.contrib.auth.decorators import login_required
from blog.models import YazilarModel
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DeleteView
from django.urls import reverse_lazy

class YaziSilDeleteView(DeleteView):
    template_name = 'pages/yazi-sil-onay.html'
    success_url = reverse_lazy('yazilarim')

    def get_queryset(self):
        yazi = YazilarModel.objects.filter(slug=self.kwargs['slug'], yazar=self.request.user)
        return yazi


'''
@login_required(login_url='/')
def yazi_sil(request, slug):
    get_object_or_404(YazilarModel, slug=slug, yazar=request.user).delete()
    return redirect('yazilarim')
'''
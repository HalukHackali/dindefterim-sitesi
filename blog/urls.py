from django.urls import path
from blog.views import KategoriListView, yazilarim, anasayfa, iletisim, DetayView, yorum_sil, YaziSilDeleteView, YaziGuncelleUpdateView, YaziEkleCreateView, onemli_siteler
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('', anasayfa, name='anasayfa'),
    path('onemli-siteler', onemli_siteler, name='onemli-siteler'),
    path('hakkimda', TemplateView.as_view(template_name="pages/hakkimda.html"), name='hakkimda'),
    path('iletisim', iletisim, name= 'iletisim'),
    path('kategori/<slug:kategoriSlug>', KategoriListView.as_view(), name='kategori'),
    path('yazilarim', yazilarim, name='yazilarim'),
    path('detay/<slug:slug>', DetayView.as_view(), name='detay'),
    path('yorum-sil/<int:id>', yorum_sil, name='yorum-sil'),
    path('yazi-ekle', YaziEkleCreateView.as_view(), name='yazi-ekle'),
    path('yazi-guncelle/<slug:slug>', YaziGuncelleUpdateView.as_view(), name='yazi-guncelle'),
    path('yazi-sil/<slug:slug>', YaziSilDeleteView.as_view(), name='yazi-sil'),

    # ÖNEMLİ SİTELER URLS
    path('meb', RedirectView.as_view(url="http://www.meb.gov.tr/"), name='meb'),



]
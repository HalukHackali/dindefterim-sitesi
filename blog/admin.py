from django.contrib import admin
from blog.models import KategoriModel, YazilarModel, YorumModel

# Register your models here.

admin.site.register(KategoriModel)

class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('baslik', 'icerik')
    list_display = ('baslik', 'olusturulma_tarihi', 'duzenlenme_tarihi', 'yazar')

admin.site.register(YazilarModel, YazilarAdmin)

class YorumAdmin(admin.ModelAdmin):
    list_display = ('yazan', 'olusturulma_tarihi', 'duzenlenme_tarihi')
    search_fields = ('yazan__username',)


admin.site.register(YorumModel, YorumAdmin)
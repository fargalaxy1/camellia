from django.contrib import admin
from website.models import *

from image_cropping import ImageCroppingMixin

# Register your models here.

class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(CategorieTe, MyModelAdmin)
admin.site.register(UnnostroTe, MyModelAdmin)
admin.site.register(AccessoriTe, MyModelAdmin)
admin.site.register(ImmaginiLocale, MyModelAdmin)
admin.site.register(ImmaginiChiSiamo, MyModelAdmin)
admin.site.register(Slider, MyModelAdmin)

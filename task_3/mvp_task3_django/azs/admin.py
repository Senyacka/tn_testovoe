from django.contrib import admin
from azs.models import (AZS,
                        Service,
                        AZSService,
                        Image,
                        AZSImage,)


admin.site.register(AZS)
admin.site.register(AZSService)
admin.site.register(Service)
admin.site.register(AZSImage)
admin.site.register(Image)

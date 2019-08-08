from django.contrib import admin

# Register your models here.
from .models import Menu,Banner,Category,Product,ProductHasImage,ProductHasReview

class ProductHasImageInline(admin.StackedInline):
    model = ProductHasImage

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductHasImageInline,
    ]

admin.site.register(Menu)
admin.site.register(Banner)
admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
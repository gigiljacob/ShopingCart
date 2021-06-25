from django.contrib import admin

from .models import ProductCategory, Product, Review


class ProductCategoryAdmin(admin.ModelAdmin):
    model = ProductCategory
    field = '__all__'
    list_display = ('category_name', 'description')
    list_per_page = 25

admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    model = Product
    field = '__all__'
    list_display = ('name', 'category', 'mrp', 'price', 'inventory', 'created_at', 'updated_at')
    list_per_page = 25

admin.site.register(Product, ProductAdmin)


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    field = '__all__'
    list_display = ('heading', 'rating', 'product', 'user')
    list_per_page = 25

admin.site.register(Review, ReviewAdmin)

from django.contrib import admin
from .models import Order, Category, Product, OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin view for Category model.

    :param admin.ModelAdmin: Inherits from Django's ModelAdmin class.
    """

    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin view for Product model.

    :param admin.ModelAdmin: Inherits from Django's ModelAdmin class.
    """

    list_display = ["name", "category", "price", "rating"]
    list_filter = ["category"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin view for Order model.

    :param admin.ModelAdmin: Inherits from Django's ModelAdmin class.
    """

    list_display = [
        "first_name",
        "last_name",
        "email",
        "address",
        "postal_code",
        "city",
        "paid",
        "created",
        "updated",
    ]
    list_filter = ["paid", "created", "updated"]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """
    Admin view for OrderItem model.

    :param admin.ModelAdmin: Inherits from Django's ModelAdmin class.
    """

    list_display = ["order", "product", "price", "quantity"]

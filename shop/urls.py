# shop/urls.py

from django.urls import path
from .views import home, MyRegisterView, logout_user, profile, category_list, cologneandbeauty, contact_thanks_view, contact_view, mens, purchase, search_products, womans, product_list, product_detail, update_random_products, product_list_by_category
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import LogoutView


app_name = 'shop'

urlpatterns = [
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_user, name='logout'),
    # path('logout_page/', logout_page, name='logout_page'),
    # path('logout/', LogoutView.as_view(next_page='shop:home'), name='logout'),
    path('register/', MyRegisterView.as_view(), name='register'),
    path('products/', product_list, name='product_list'),
    path('update-random-products/', update_random_products, name='update_random_products'),
    path('products/<slug:category_slug>/', product_list_by_category, name='product_list_by_category'),
    path('products/<int:id>/<slug:slug>/', product_detail, name='product_detail'),
    path('purchase/', purchase, name='purchase'),
    path('womans/', womans, name='womans'),
    path('mens/', mens, name='mens'),
    path('cologneandbeauty/', cologneandbeauty, name='cologneandbeauty'),
    path('categories/', category_list, name='categories'),
    path('contact/', contact_view, name='contact'),
    path('contact/thanks/', contact_thanks_view, name='contact_thanks'),
    path('search/', search_products, name='search_products'),
]









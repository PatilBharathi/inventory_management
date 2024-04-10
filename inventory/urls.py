from django.urls import re_path
from .views import *


urlpatterns = [

    re_path(r'^$', index, name='index'),

    re_path(r'^display_laptops$', display_laptops, name='display_laptops'),
    re_path(r'^display_desktops$', display_desktops, name='display_desktops'),
    re_path(r'^display_mobiles$', display_mobiles, name='display_mobiles'),

    re_path(r'^add_laptop$', add_laptop, name='add_laptop'),
    re_path(r'^add_desktop$', add_desktop, name='add_desktop'),
    re_path(r'^add_mobile$', add_mobile, name='add_mobile'),

    re_path(r'^edit_laptop/(?P<pk>\d+)$', edit_laptop, name='edit_laptop'),
    re_path(r'^edit_desktop/(?P<pk>\d+)$', edit_desktop, name='edit_desktop'),
    re_path(r'^edit_mobile/(?P<pk>\d+)$', edit_mobile, name='edit_mobile'),

    re_path(r'^delete_laptop/(?P<pk>\d+)$', delete_laptop, name='delete_laptop'),
    re_path(r'^delete_desktop/(?P<pk>\d+)$', delete_desktop, name='delete_desktop'),
    re_path(r'^delete_mobile/(?P<pk>\d+)$', delete_mobile, name='delete_mobile')

]
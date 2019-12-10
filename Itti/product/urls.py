from . import views
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('show/',views.show),
    url('shreeza/',views.bibisha),
    url('product/',views.product),
    url(r'^delete/(?P<id>\d+)/$',views.destroy),
    url(r'^edit/(?P<id>\d+)/$',views.edit),
    url(r'^update/(?P<id>\d+)$',views.update),
    url('raw_sql/',views.raw_sql),
    url('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name="logout")
]

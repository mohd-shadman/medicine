
from django.contrib import admin
from django.urls import path
from doctor import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('post/',views.post,name='post'),
    path('post/',views.success,name='success'),
    path('older/',views.older,name='older'),
    path('syrup/',views.syrup,name='syrup'),
    path('tablets/',views.tablets,name='tablets'),
    path('injection/',views.injection,name='injection'),
    path('orders/',views.orders,name='orders'),
    path('booking/',views.booking,name='booking'),
    path('getvalue/',views.getvalue,name='getvalue'),
    
]+static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

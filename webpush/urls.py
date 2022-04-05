from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^save_information', views.save_info, name='save_webpush_info'),
    # Service worker need to be loaded from same domain
    re_path(r'^service-worker.js', views.ServiceWorkerView.as_view(), name='service_worker')
]

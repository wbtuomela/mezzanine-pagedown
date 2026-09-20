try:
    from django.urls import re_path
except ImportError:  # Django < 1.10
    from django.conf.urls import url as re_path

from .views import MarkupPreview

urlpatterns = [re_path(r'^preview/$', MarkupPreview.as_view(), name='preview'), ]

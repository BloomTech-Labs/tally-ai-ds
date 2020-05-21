# yelp/urls.py

from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
# view functions
from .views import home
from .views import hello
from .views import YelpYelpScrapingCreateView
from .views import YelpYelpScrapingDetailsView


urlpatterns = {
    path('<slug:business_id>', home, name='home'),
    path('', hello, name='hello'),
    # example- for mannually adding reviews
    url(r'^review/$', YelpYelpScrapingCreateView.as_view(), name="create"),
    url(r'^review/(?P<pk>[0-9a-f-]+)/$',
        YelpYelpScrapingDetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
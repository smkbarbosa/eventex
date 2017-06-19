from django.conf.urls import include, url

from eventex.subscriptions.views import detail
from eventex.subscriptions.views import new

urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^(\d+)/$', detail, name='detail'),
]
from django.conf.urls import url

from datasets import views

app_name = 'datasets'

urlpatterns = [
    url(r'^$',
        views.portal,
        name='portal'),

    url(r'^new_dataset/$',
        views.dataset_create,
        name='dataset_create'),

    url(r'^(?P<slug>[-\w]*)-(?P<pk>[0-9]+)/update/$',
        views.dataset_update,
        name='dataset_update'),

    url(r'^(?P<slug>[-\w]*)-(?P<pk>[0-9]+)/remove/$',
       views.DatasetRemove.as_view(),
        name='dataset_remove'),

#    url(r'^(?P<slug>[-\w]*)-(?P<pk>[0-9]+)/remove/$',
#        views.dataset_remove,
#        name='dataset_remove'),

    url(r'^(?P<slug>[-\w]*)-(?P<pk>\d+)/$',
        views.dataset_detail,
        name='dataset_detail'),
]

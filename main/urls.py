from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
# admin
# datasets and accounts together

    url(r'^admin/', admin.site.urls),

    url(r'^about/$',
        TemplateView.as_view(template_name="about.html"),
        name="about"),

    url(r'^contact/$',
        TemplateView.as_view(template_name="contact.html"),
        name="contact"),

    # the portal view should be here

    url(r'^',
        include('accounts.urls',
        namespace='accounts')),

    # hopefully this will work.
    url(r'^',
        include('datasets.urls',
        namespace='datasets')),

]

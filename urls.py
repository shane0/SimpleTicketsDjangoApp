from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^my_admin/jsi18n', 'django.views.i18n.javascript_catalog'), # for AdminDateWidget
    (r'^$', 'mysite.billing.views.home'),
    (r'^admin/', include(admin.site.urls)),
    (r'^billing/(?P<invoice_id>\d+)', 'mysite.billing.views.invoices_detail'),
    (r'^billing/', 'mysite.billing.views.invoices'),

)


from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.views import generic
from rest_framework.schemas import get_schema_view


router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'states', views.StateViewSet)
router.register(r'renters', views.RenterViewSet)
router.register(r'owners', views.OwnerViewSet)
router.register(r'invoices', views.InvoiceViewSet)
router.register(r'primarycolors', views.PrimaryColorViewSet)
router.register(r'secondarycolors', views.SecondaryColorViewSet)
router.register(r'costumes', views.CostumeViewSet)
router.register(r'timeperiods', views.TimePeriodViewSet)
router.register(r'sizes', views.SizeViewSet)
router.register(r'shows', views.ShowViewSet)

#Login URLs for browsable API
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^$', generic.RedirectView.as_view(url='/api/', permanent=False)),
    url(r'^api/$', get_schema_view()),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
]

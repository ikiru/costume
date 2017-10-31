from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(title='Construction API')

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'states', views.StateViewSet)
router.register(r'organizations', views.OrganizationsViewSet)
router.register(r'renters', views.RentersViewSet)
router.register(r'owners', views.OwnersViewSet)
router.register(r'events', views.EventsViewSet)
router.register(r'primarycolors', views.PrimaryColorsViewSet)
router.register(r'secondarycolors', views.SecondaryColorsViewSet)
router.register(r'costumes', views.CostumesViewSet)
router.register(r'timeperiods', views.TimePeriodsViewSet)
router.register(r'sizes', views.SizesViewSet)
router.register(r'shows', views.ShowsViewSet)

#Login URLs for browsable API
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), JWT URLs
    # url(r'^api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh' ), JWT Urls
    url(r'^schema/$', schema_view), # For api schema view
]

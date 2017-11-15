from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from rest_framework.schemas import get_schema_view
from rest_framework_jwt.views import obtain_jwt_token

# from rest_framework.authtoken import views as drf_views


schema_view = get_schema_view(title='Construction API')

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
    url(r'^api-token-auth/', obtain_jwt_token),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	## enable authentication endpoints
	# url(r'^auth$', drf_views.obtain_auth_token, name='auth'),
	# url(r'^api/auth/token/obtain/$', TokenObtainPairView.as_view()),
    # url(r'^api/auth/token/refresh/$', TokenRefreshView.as_view()),
    url(r'^schema/$', schema_view), # For api schema view
]


## to get token from terminal
## curl -X POST -d "email=email&password=password" http://localhost:8000/api/token/

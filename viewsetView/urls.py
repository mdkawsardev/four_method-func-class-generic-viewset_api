from rest_framework.routers import DefaultRouter
from viewsetView.views import *

router = DefaultRouter()
router.register(r"viewuser", UserViewset, basename='viewuser')

urlpatterns = router.urls

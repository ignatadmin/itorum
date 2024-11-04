from rest_framework.routers import DefaultRouter

from .views import ClientViewSet, MailingViewSet, MessageViewSet


router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'mailings', MailingViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = router.urls

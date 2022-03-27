
from .viewset import AppointmentViewset, ContactViewset
from rest_framework import routers

router = routers.DefaultRouter()

router.register('appointment', AppointmentViewset, "appointment")
router.register('contact', ContactViewset, "contact")

urlpatterns = router.urls
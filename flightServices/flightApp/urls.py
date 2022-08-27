from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PassengerViewSet, FlightViewSet, ReservationViewSet

router = DefaultRouter()
router.register('flights', FlightViewSet)
router.register('passengers', PassengerViewSet)
router.register('reservations', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PassengerViewSet, FlightViewSet, ReservationViewSet, find_flight, save_reservation
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('flights', FlightViewSet)
router.register('passengers', PassengerViewSet)
router.register('reservations', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('findFlights', find_flight),
    path('saveReservation', save_reservation),
    path('api-token-auth/', obtain_auth_token, name="api_token_auth")
]
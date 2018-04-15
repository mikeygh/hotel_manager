from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import views

# URL Patterns

urlpatterns = [
    # this endpoint will list all hotel entries from the database.
    url(r'hotels/$', views.HotelList.as_view()),
    # This endpoint will show all reservations in the datatbase
        # As well as allowing for hotel to be created via a POST.
    url(r'reservations/$', views.ReservationList.as_view(), name='get_post_reservations'),
    # This last endpoint, is a helper endpoint to edit a specific hotel object.
    url(r'hotel_edit/(?P<pk>[0-9]+)$', views.HotelEdit.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

from django.urls import path
from .views import GenerateData, EventDisplay, GetDate
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", GetDate, name ="Retrieve Data"),
    path("/Generate_Report/", GenerateData, name ="Generate Report"),
    path("events/<int:pk>/", EventDisplay.as_view(), name='event_display')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
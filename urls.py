from django.urls import path

from . import views

urlpatterns = [
  path('', views.HomeView.as_view(), name='home'),
  path("lines/", views.LinesView.as_view(), name="lines"),
  path('lines/<pk>/delete/', views.DeleteLineView.as_view(), name="delete_line"),
  path('lines/new/', views.CreateLineView.as_view(), name="create_line"),
  path('lines/<pk>/update/', views.UpdateLineView.as_view(), name="update_line"),
  path('stations/', views.StationsView.as_view(), name="stations"),
  path('stations/<pk>/update/', views.UpdateStationView.as_view(), name="update_station"),
  path('stations/<pk>/delete/', views.DeleteStationView.as_view(), name="delete_station"),
  path('stations/new/', views.CreateStationView.as_view(), name="create_station"),
  path('stops/', views.StopsView.as_view(), name="stops"),
  path('stops/new/', views.CreateStop.as_view(), name="create_stop"),
  path('stops/<pk>/update', views.UpdateStop.as_view(), name="update_stop"),
  path('stops/<pk>/delete', views.DeleteStop.as_view(), name="delete_stop")
]

from django.urls import path
from web import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
    path("booking/", views.booking, name="booking"),
    path("reviews/", views.reviews, name="reviews"),
    path("amenities/", views.amenities, name="amenities"),
    path("contact/", views.contact, name="contact"),
    path("rooms/<int:id>", views.rooms, name="rooms"),
    path("boock-recived/", views.boock_recived, name="boock-recived"),
]
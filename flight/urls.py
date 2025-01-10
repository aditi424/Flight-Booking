from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("query/places/<str:q>", views.query, name="query"),
    path("flight", views.flight, name="flight"),
    path("review", views.review, name="review"),
    path("flight/ticket/book", views.book, name="book"),
    path("flight/ticket/payment", views.payment, name="payment"),
    path('flight/ticket/api/<str:ref>', views.ticket_data, name="ticketdata"),
    path('flight/ticket/print',views.get_ticket, name="getticket"),
    path('flight/bookings', views.bookings, name="bookings"),
    path('flight/ticket/cancel', views.cancel_ticket, name="cancelticket"),
    path('flight/ticket/resume', views.resume_booking, name="resumebooking"),
    path('contact', views.contact, name="contact"),
    path('privacy-policy', views.privacy_policy, name="privacypolicy"),
    path('terms-and-conditions', views.terms_and_conditions, name="termsandconditions"),
    path('about-us', views.about_us, name="aboutus"),
    #admin 
    path("adminlogin", views.admin_login_view, name="adminlogin"),
    path("adminregister", views.admin_register_view, name="adminregister"),
    path('admindashboard/', views.admin_dashboard, name='admindashboard'),
    #path('dashboard/', views.flight_place_dashboard, name='flight_place_dashboard'),
    #path("admin/dashboard", views.admin_dashboard, name="admin_dashboard"),
    
    path('manage-flights/', views.manage_flights, name='manage_flights'),
    path('edit-flight/<int:id>/', views.edit_flight, name='edit_flight'),
    path('delete-flight/<int:id>/', views.delete_flight, name='delete_flight'),
    
]
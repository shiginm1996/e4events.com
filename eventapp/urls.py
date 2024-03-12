from django.urls import path
from .views import *

urlpatterns=[
    path('sample/',sample),
    path('index/',event_index),
    path('userlogin/',user_login),
    path('seller_user_display/',seller_user_display),
    path('user_reg/',user_reg),
    path('sellerprofedit/<int:id>',profile_edit),
    path('customerprofedit/<int:id>',customer_edit),
    path('sellerlogout/',logoutfun),
    path('eventteam/',customer_profile),
    path('eventbooking/<int:id>',eventbooking),
    path('company_page/',event_company_page),
    # path('bookingstatus/<int:id>',booking_status)
    path('booking_status/<int:id>',confirm_book),
    # path('confirm/',confirm_displayu),
    path('customer_prof/',customer_dis),
    path('review_edit/<int:id>',review_edit),
    path('review_delete/<int:id>',delete_review),
    path('admin_log/',admin_login),
    path('admin_page/',admin_page),
    path('admin_reg/',admin_reg),
    path('adminlogout/',admin_logoutfun),
    path('adminuser/<int:id>',admin_user_prof),
    path('first/',gallery),
    path('contact/',contact),
    path('about/',about),
    path('second/', gallery2),
    path('payment/<int:id>',payment),
    path('successpage/',successfun)
]


from django.urls import path
from .views import *
from django.urls import path
from core import views
from .models import *

urlpatterns = [
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('user', UserAPIView.as_view()),
    path('refresh', RefreshAPIView.as_view()),
    path('logout', LogoutAPIView.as_view()),
    path('forgot', ForgotAPIView.as_view()),
    path('reset', ResetAPIView.as_view()),
     path('profile',views.ProfileList.as_view()),
    path('profile/details/<str:pk>',views.ProfileDetail.as_view()),
    path('feeds',views.FeedsList.as_view()),
    path('feeds/details/<str:pk>',views.FeedsDetail.as_view()),
    path('merchandise',views.MerchandiseList.as_view()),
    path('merchandise/details/<str:pk>',views.MerchandiseDetail.as_view()),
    path('category',views.CategoryList.as_view()),
    path('category/details/<str:pk>',views.CategoryDetail.as_view()),
    path('comment',views.CommentList.as_view()),
    path('comment/details/<str:pk>',views.CommentDetail.as_view()),

]
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('booking/', include(router.urls)),
    path('menu/', views.MenuView.as_view()),
    path('menu-items/', views.MenuItemsView.as_view(), name = "menu-items"),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view())
]
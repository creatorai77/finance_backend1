from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet
from finance.views import FinancialRecordViewSet, DashboardSummaryView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('records', FinancialRecordViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),

    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

    # ✅ Correct place for dashboard
    path('api/dashboard/summary/', DashboardSummaryView.as_view()),
]
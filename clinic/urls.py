from django.urls import path
from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import index, UserProfileViewSet, DoctorRegisterViewSet, DoctorListViewSet, \
                DoctorRetrieveViewSet, PatientRegisterViewSet, PatientRetrieveViewSet, ReviewViewSet, \
                AppointmentViewSet, UserImageViewSet, VerifyUserViewSet

router = SimpleRouter()
router.register('auth/users', UserProfileViewSet, basename='users')
router.register('users/images', UserImageViewSet, basename='users-images')
router.register('users', VerifyUserViewSet, basename='users-verify')
router.register('doctors/register', DoctorRegisterViewSet, basename='doctors-register')
router.register('doctors', DoctorListViewSet, basename='doctors')
router.register('doctors', DoctorRetrieveViewSet, basename='doctors')
doctors_router = NestedSimpleRouter(router, r'doctors', lookup='doctors')
doctors_router.register(r'reviews', ReviewViewSet, basename='doctors-reviews')

router.register('patients/register', PatientRegisterViewSet, basename='patients-register')
router.register('patients', PatientRetrieveViewSet, basename='patients')

router.register('appointments/create', AppointmentViewSet, basename='appoinments-create')

urlpatterns = [path('', index),
               path('auth/signin/', TokenObtainPairView.as_view()),
                path('auth/refresh/', TokenRefreshView.as_view())
               ] + router.urls + doctors_router.urls

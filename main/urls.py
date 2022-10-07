from django.urls import path, include
from .views import *


urlpatterns = [
    path('courses', Home.as_view(), name='courses'),
    path('my_crss', GetSelfCourses.as_view(), name='my_crss'),
    path('course/<str:slug>/', GetCourse.as_view(), name='course'),
    path('lesson/<str:slug>/', GetLesson.as_view(), name='lessons_by_course'),
    path('', index, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('lk/', lk, name='lk'),
    path('lesson_complete/', lesson_complete, name='lesson_complete'),
    path('tutors/', tutors, name='tutors'),
    path('contact/', contact, name='contact'),
    path('pricing/', pricing, name='pricing'),
]
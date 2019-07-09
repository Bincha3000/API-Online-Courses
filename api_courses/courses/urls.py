from django.urls import path

from courses.views import AllCoursesView, OneCourseView, CategoriesView, TeachersView, PersonalArea


app_name = 'courses'
urlpatterns = [
    path('', AllCoursesView.as_view(), name='courses'),
    path('<int:pk>', OneCourseView.as_view(), name='course'),
    path('categories', CategoriesView.as_view(), name='categories'),
    path('teachers', TeachersView.as_view(), name='teachers'),
    path('profile', PersonalArea.as_view(), name='profile')
]

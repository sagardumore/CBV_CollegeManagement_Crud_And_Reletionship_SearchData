from django.urls import path
from .import views

urlpatterns = [
    path('add_department/',views.AddDepartmentView.as_view(),name='add_department'),
    path('show_department/', views.ShowDepartmentView.as_view(), name='show_department'),
    path('add_professor/', views.AddProfessorView.as_view(), name='add_professor'),
    path('show_professor/', views.ShowProfessorView.as_view(), name='show_professor'),
    path('add_student/', views.AddStudentView.as_view(), name='add_student'),
    path('show_student/', views.ShowStudentView.as_view(), name='show_student'),

    path('update_department/<int:i>/',views.DepartmentUpdateView.as_view(),name='update_department'),
    path('delete_department/<int:i>/',views.DepartmentDeleteView.as_view(),name='delete_department'),

    path('update_professor/<str:i>/',views.ProfessorUpdateView.as_view(),name='update_professor'),
    path('delete_professor/<str:i>/',views.ProfessorDeleteView.as_view(),name='delete_professor'),

    path('update_student/<int:i>/',views.StudentUpdateView.as_view(),name='update_student'),
    path('delete_student/<int:i>/',views.StudentDeleteView.as_view(),name='delete_student'),

]
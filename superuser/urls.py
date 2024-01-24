from django.urls import path
from . import views

urlpatterns = [
    path("", views.s_login, name="s_login"),
    path("logout/", views.s_logout, name="s_logout"),
    path("frgtpswd/", views.s_frgtpswd, name="s_frgtpswd"),
    path("dashboard/", views.s_dashboard, name="s_dashboard"),
    path("courses/", views.s_courses, name="s_courses"),
    path("courseDtail/<uuid:pk>", views.s_courseDetail, name="s_courseDetail"),
    path("crsActiv/<uuid:pk>", views.s_courseActivate, name="s_courseActivate"),
    path("crsDeactiv/<uuid:pk>", views.s_courseDeactivate, name="s_courseDeactivate"),
    path("crsDel/<uuid:pk>", views.s_courseDelete, name="s_courseDelete"),
    path("addLearn/", views.s_addLearn, name="s_addLearn"),
    path("faculty/", views.s_faculty, name="s_faculty"),
    path("fcltyDtail/<uuid:pk>", views.s_facultyDetail, name="s_facultyDetail"),
    path("fcltyActiv/<uuid:pk>", views.s_facultyActivate, name="s_facultyActivate"),
    path("fcltyDeactiv/<uuid:pk>", views.s_facultyDeactivate, name="s_facultyDeactivate"),
    path("fcltyDel/<uuid:pk>", views.s_facultyDelete, name="s_facultyDelete"),
    path("student/", views.s_student, name="s_student"),
    path("stdSrch/", views.s_studentSearch, name="s_studentSearch"),
    path("stdEdit/<uuid:pk>", views.s_studentEdit, name="s_studentEdit"),
    path("stdDel/<uuid:pk>", views.s_studentDelete, name="s_studentDelete"),
    path("stdActiv/<uuid:pk>", views.s_studentActivate, name="s_studentActivate"),
    path("stdDeactiv/<uuid:pk>", views.s_studentDeactivate, name="s_studentDeactivate"),
    path("batch/", views.s_batch, name="s_batch"),
    path("bachAssign/<uuid:pk>", views.s_batchAssign, name="s_batchAssign"),
    path("batchDtail/<uuid:pk>", views.s_batchDetail, name="s_batchDetail"),
    path("batchActiv/<uuid:pk>", views.s_batchActivate, name="s_batchActivate"),
    path("batchDeactiv/<uuid:pk>", views.s_batchDeactivate, name="s_batchDeactivate"),
    path("batchDel/<uuid:pk>", views.s_batchDelete, name="s_batchDelete"),
    path("profile/", views.s_profileUpdate, name="s_profileUpdate"),
    path("profilepswd/", views.s_paswrdUpdate, name="s_paswrdUpdate"),
]

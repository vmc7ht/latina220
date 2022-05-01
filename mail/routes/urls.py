from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf.urls import url


urlpatterns = [
    path('weekly/20109/<int:week>', views.dashboardView, name="weekly"),
    path('weekly/20109/-<int:week>', views.dashboardView, name="weekly"),
    path('weekly/20110/<int:week>', views.dashboardView, name="weekly"),
    path('weekly/20110/-<int:week>', views.dashboardView, name="weekly"),


    path('weekly/20109/<int:week>/employee_add', views.RouteCreate.as_view(), name="route"),
    path('weekly/20109/-<int:week>/employee_add', views.RouteCreate.as_view(), name="route"),
    path('weekly/20110/<int:week>/employee_add', views.RouteCreate.as_view(), name="route"),
    path('weekly/20110/-<int:week>/employee_add', views.RouteCreate.as_view(), name="route"),

    path('ajax/update_name/',views.update_name, name='update_name'),
    path('ajax/update_route_number/',views.update_route_number, name='update_route_number'),
    path('ajax/update_override/',views.update_override, name='update_override'),
    path('ajax/update_t6_override/',views.update_t6_override, name='update_t6_override'),
    path('ajax/update_t6_type/',views.update_t6_type, name='update_t6_type'),
    path('ajax/update_t6_name/',views.update_t6_name, name='update_t6_name'),

    path('weekly/20109/<int:week>/employee_delete', views.deleteView, name="route"),
    path('weekly/20109/-<int:week>/employee_delete', views.deleteView, name="route"),
    path('weekly/20110/<int:week>/employee_delete', views.deleteView, name="route"),
    path('weekly/20110/-<int:week>/employee_delete', views.deleteView, name="route",),


    path('weekly/20109/<int:week>/employee_edit', views.editView, name="route"),
    path('weekly/20109/-<int:week>/employee_edit', views.editView, name="route"),
    path('weekly/20110/<int:week>/employee_edit', views.editView, name="route"),
    path('weekly/20110/-<int:week>/employee_edit', views.editView, name="route",),


    path('weekly/20109/<int:week>/employee_edit/<int:route_id>/<str:name>/<int:route_num>', views.RouteEdit.as_view(), name="route"),
    path('weekly/20109/-<int:week>/employee_edit/<int:route_id/<str:name>/<int:route_num>>', views.RouteEdit.as_view(), name="route"),
    path('weekly/20110/<int:week>/employee_edit/<int:route_id>/<str:name>/<int:route_num>', views.RouteEdit.as_view(), name="route"),
    path('weekly/20110/-<int:week>/employee_edit/<int:route_id/<str:name>/<int:route_num>>', views.RouteEdit.as_view(), name="route",),

    path('weekly/20109/<int:week>/employee_delete/<int:route_id>/<str:name>/<int:route_num>', views.RouteDelete.as_view(), name="route"),
    path('weekly/20109/-<int:week>/employee_delete/<int:route_id/<str:name>/<int:route_num>>', views.RouteDelete.as_view(), name="route"),
    path('weekly/20110/<int:week>/employee_delete/<int:route_id>/<str:name>/<int:route_num>', views.RouteDelete.as_view(), name="route"),
    path('weekly/20110/-<int:week>/employee_delete/<int:route_id/<str:name>/<int:route_num>>', views.RouteDelete.as_view(), name="route",),

    path('weekly/20109/<int:week>/employee_delete/t6/<str:name>/<int:t6id>', views.delete_t6_view, name="route"),
    path('weekly/20109/-<int:week>/employee_delete/t6/<str:name>/<int:t6id>>', views.delete_t6_view, name="route"),
    path('weekly/20110/<int:week>/employee_delete/t6/<str:name>/<int:t6id>', views.delete_t6_view, name="route"),
    path('weekly/20110/-<int:week>/employee_delete/t6/<str:name>/<int:t6id>>', views.delete_t6_view, name="route",),    
]

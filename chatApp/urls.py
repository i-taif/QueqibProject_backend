from django.urls import path
from . import views
urlpatterns = [
    path('list-all-meassge',views.list_all_message,name='list-all-message'),
    path('create-message',views.create_message,name='create-message'),
    path('list-message/<id>',views.message_list,name='message-list'),
    path('create-service',views.add_service,name='create-service'),
    path('list-service/<user_id>',views.list_services_by_TourGuide,name='list-service'),
    path('list-service',views.list_all_services,name='list-service'),
    path('update-service/<id>',views.update_service,name='apdate-service'),
    path('delete-service/<id>',views.delete_service,name='delete-service'),
    path('create-rete',views.add_rate,name='create-rate'),
    path('list-rete/<user_id>',views.list_Rate,name='list-rate'),




    # URL form "users/1"
    #path('users/<int:pk>', views.user_list, name='user-detail'),      # GET request for user with id
    #path('users', views.user_list, name='user-list'),    # POST for new user and GET for all users list

]
from django.urls import path, include

from apps.posts.views import PostAPIView ,PostCreateAPI, PostRetrieveAPI, PostDestroyAPI,PostUpdateAPI


urlpatterns = [
    path('', PostAPIView.as_view(), name="api_posts"),
    path('<int:pk>', PostRetrieveAPI.as_view(), name="api_retrieve_post"),
    path('create/', PostCreateAPI.as_view(), name="api_create_post"),
    path('update/<int:pk>/', PostUpdateAPI.as_view(), name="api_update_post"),
    path('destroy/<int:pk>/', PostDestroyAPI.as_view(), name="api_destroy_post"),
]
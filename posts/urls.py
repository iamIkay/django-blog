from django.urls import include

urlpatterns = [
    path('', include('posts.urls'))
]
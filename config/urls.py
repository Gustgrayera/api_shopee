from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers

from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
#users_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
#users_router.register(r'todos', views.TodosViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

urlpatterns += router.urls
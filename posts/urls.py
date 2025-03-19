from django.urls import path
from posts import views


urlpatterns = [
    path("<int:pk>/edit/", views.PostUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="delete"),
    path("create/", views.PostCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", views.PostDetailView.as_view(), name="detail"),
    path("list/", views.PostListView.as_view(), name="list"),
]
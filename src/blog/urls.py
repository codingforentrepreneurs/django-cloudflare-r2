from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.blog_post_list_view, name="post-list"),
    path("<int:id>/", views.blog_post_detail_view, name="post-detail"),
]

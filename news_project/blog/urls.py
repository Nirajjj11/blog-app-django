from django.urls import path
from .views import *

urlpatterns = [
      path("", BlogListView.as_view(), name="blog_list"),
      path("pending/", PendingListView.as_view(), name="pending"),

      path("new/", BlogCreateView.as_view(), name="blog_new"),
      path("<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
      path("<int:pk>/edit/", BlogUpdateView.as_view(), name="blog_edit"),
      path("<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),

      path("<int:pk>/submit/", submit_review, name="submit_review"),
      path("<int:pk>/approve/", approve_blog, name="approve_blog"),
      path("<int:pk>/reject/", reject_blog, name="reject_blog"),

      path("<int:pk>/like/", like_blog, {"value": 1}, name="like"),
      path("<int:pk>/dislike/", like_blog, {"value": -1}, name="dislike"),
      path("<int:pk>/comment/", add_comment, name="comment"),
]
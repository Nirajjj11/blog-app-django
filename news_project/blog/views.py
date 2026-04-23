from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Blog, Comment, Like


class BlogListView(ListView):
      model = Blog
      template_name = "blog/blog_list.html"
      context_object_name = "blogs"   

      def get_queryset(self):
            return Blog.objects.filter(status="published").order_by('-created_at')


class BlogDetailView(DetailView):
      model = Blog
      template_name = "blog/blog_detail.html"


class BlogCreateView(LoginRequiredMixin, CreateView):
      model = Blog
      fields = ['title', 'body', 'image']
      template_name = "blog/blog_form.html"

      def form_valid(self, form):
            form.instance.author = self.request.user
            form.instance.status = "draft"
            return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
      model = Blog
      fields = ['title', 'body','image']
      template_name = "blog/blog_form.html"


class BlogDeleteView(LoginRequiredMixin, DeleteView):
      model = Blog
      template_name = "blog/blog_delete.html"
      success_url = reverse_lazy("blog_list")


# AUTHOR ACTION
def submit_review(request, pk):
      blog = Blog.objects.get(pk=pk)
      if request.user == blog.author:
            blog.status = "pending"
            blog.save()
      return redirect("blog_detail", pk=pk)


# EDITOR PANEL
class PendingListView(UserPassesTestMixin, ListView):
      model = Blog
      template_name = "blog/pending_list.html"

      def test_func(self):
            return self.request.user.is_editor or self.request.user.is_superuser

      def get_queryset(self):
            return Blog.objects.filter(status="pending")


def approve_blog(request, pk):
      blog = Blog.objects.get(pk=pk)
      if request.user.is_editor or request.user.is_superuser:
            blog.status = "published"
            blog.save()
      return redirect("pending")


def reject_blog(request, pk):
      blog = Blog.objects.get(pk=pk)
      if request.user.is_editor:
            blog.status = "rejected"
            blog.save()
      return redirect("pending")


# LIKE / DISLIKE
def like_blog(request, pk, value):
      blog = Blog.objects.get(pk=pk)
      Like.objects.update_or_create(
            blog=blog,
            user=request.user,
            defaults={"value": value}
      )
      return redirect("blog_detail", pk=pk)


# COMMENT
def add_comment(request, pk):
      if request.method == "POST":
            blog = Blog.objects.get(pk=pk)
            text = request.POST.get("text")
            Comment.objects.create(blog=blog, user=request.user, text=text)
      return redirect("blog_detail", pk=pk)
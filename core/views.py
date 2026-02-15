from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Post
from .forms import PostForm

User = get_user_model()

def home(request):
    posts = Post.objects.order_by("-created_at")

    paginator = Paginator(posts, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "core/home.html", {"page_obj": page_obj})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "core/post_detail.html", {"post": post})

@login_required
def post_create(request):
    form = PostForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect("home")

    return render(request, "core/post_create.html", {"form": form})

@login_required
def post_update(request, id):
    post = get_object_or_404(Post, id=id)

    if request.user != post.author:
        messages.error(request, "Bu postu düzenleme yetkiniz yok.")
        return redirect("post_detail", id=post.id)

    form = PostForm(request.POST or None, instance=post)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Post başarıyla güncellendi.")
        return redirect("post_detail", id=post.id)

    return render(request, "core/post_update.html", {"form": form})

@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)

    if request.user != post.author:
        messages.error(request, "Bu postu silme yetkiniz yok.")
        return redirect("post_detail", id=post.id)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post başarıyla silindi.")
        return redirect("home")

    return render(request, "core/post_delete.html", {"post": post})

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("home")

    return render(request, "core/register.html", {"form": form})

@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")

    return render(request, "core/logout.html")

def post_search(request):
    query = request.GET.get("q")
    posts = Post.objects.none()

    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).order_by("-created_at")

    return render(request, "core/post_search.html", {
        "query": query,
        "posts": posts
    })

def profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    user_posts = Post.objects.filter(author=profile_user).order_by("-created_at")

    return render(request, "core/profile.html", {
        "profile_user": profile_user,
        "user_posts": user_posts
    })

def user_search(request):
    query = request.GET.get("q")
    users = User.objects.none()

    if query:
        users = User.objects.filter(
            username__icontains=query
        ).order_by("username")

    return render(request, "core/user_search.html", {
        "query": query,
        "users": users
    })

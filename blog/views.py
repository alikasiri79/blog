from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import NewPostForm
from django.views import generic
from django.urls import reverse_lazy


# Create your views here.


# def post_list_view(request):
#     posts_list = Post.objects.filter(status='pub')
#     return render(request, 'blog/post_list_view.html', {'posts_list': posts_list})
class PostListView(generic.ListView):
    template_name = 'blog/post_list_view.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub')


# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


# def post_create_view(request):
#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#     else:
#
#         form = NewPostForm()
#     return render(request, 'blog/post_create.html', {'form': form})
class PostCreateView(generic.CreateView):
    form_class = NewPostForm
    template_name = 'blog/post_create.html'


# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = NewPostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('post_detail', pk=pk)
#
#     return render(request, 'blog/post_create.html', {'form': form})
class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = NewPostForm
    template_name = 'blog/post_create.html'


# def post_delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post_list')
#
#     return render(request, 'blog/post_delete.html', context={'post': post})
class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')
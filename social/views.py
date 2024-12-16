from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post
from groups.models import Grupo
from django.utils import timezone

@login_required
def criar_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, user=request.user)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.data = timezone.now()
            post.save()
            return redirect('listar_posts_grupo', grupo_id=post.grupo.id)
    else:
        form = PostForm(user=request.user)
    return render(request, 'social/criar_post.html', {'form': form})

@login_required
def listar_posts_grupo_view(request, grupo_id):
    grupo = get_object_or_404(Grupo, id=grupo_id, membros=request.user)
    posts = Post.objects.filter(grupo=grupo).order_by('-data')  # Posts mais recentes primeiro
    return render(request, 'social/listar_posts_grupo.html', {'grupo': grupo, 'posts': posts})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Blog, Comment


# Existing views...
def blog(request):
    return render(request, 'blog/blog.html', {'blogs': Blog.objects.all()})

def blog_single(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'blog/blog_single.html', {'blog': blog})

def add_comment(request, blog_id):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to comment.")
            return redirect('login')
        
        blog = get_object_or_404(Blog, pk=blog_id)
        comment_text = request.POST.get('comment')
        parent_id = request.POST.get('parent_id')
        parent = None

        if parent_id:
            parent = Comment.objects.get(id=parent_id)

        if comment_text:
            comment = Comment.objects.create(
                user=request.user,
                blog=blog,
                comment=comment_text,
                parent=parent
            )
            comment.save()
            messages.success(request, "Your comment has been posted.")
        else:
            messages.error(request, "Comment cannot be empty.")
    
    return redirect('blog_single', id=blog_id)

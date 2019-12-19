from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import date


from .models import post, like, comment, categories
from .forms import CommentForm
# Create your views here.

def BlogHomeView(request):
    all_categories = categories.objects.all()
    all_posts = post.objects.order_by('-date')
    search_term = ''
    

    if 'category' in request.GET:
        selected_category_title = page = request.GET.get('category')
        all_posts = all_posts.filter(category__title = selected_category_title)
    
    if 'search' in request.GET:
        search_term = request.GET['search']
        all_posts = all_posts.filter(title__icontains = search_term)

    paginator = Paginator(all_posts, 5)

    page = request.GET.get('page')
    all_posts = paginator.get_page(page)

    get_dict_copy = request.GET.copy()
    params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()
    context = {
        'categories': all_categories,
        'posts': all_posts,
        'params': params, 
        'search_term': search_term
    }
    return render(request, 'bloghome.html', context)


def BlogPostView(request, slug):
    slug_post = post.objects.filter(slug=slug)[0]
    comments = comment.objects.filter(post = slug_post)
    all_categories = categories.objects.all()

    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = comment()
                new_comment.comment_text = form.cleaned_data.get('comment_text')
                new_comment.post = slug_post
                new_comment.date = date.today()
                new_comment.user = request.user
                new_comment.save()
                messages.success(
                                request,
                                'Comment Added Successfully',
                                extra_tags='alert alert-success alert-dismissible fade show'
                                )
                return redirect('blog:post', slug)
        else:
            messages.success(
                                request,
                                'Login to add a comment',
                                extra_tags='alert alert-success alert-dismissible fade show'
                                )
            return redirect('blog:post', slug)
    else:
        form = CommentForm()
        context = {
            'form': form,
            'post': slug_post,
            'comments': comments,
            'categories': all_categories,
        }
        return render(request, 'blogpost.html', context)

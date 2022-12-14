from django.db.models import Count, Q
from django.shortcuts import render
from .models import Blog, Tag, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog_list(request):
    blogs = Blog.objects.all()

    category = request.GET.get('category')
    if category:
        blogs = Blog.objects.filter(category__title__exact=category)

    tag = request.GET.get('tag')
    if tag:
        blogs = Blog.objects.filter(tag__title__exact=tag)

    q = request.GET.get('q')
    if q:
        blogs = Blog.objects.distinct().filter(
            Q(title__icontains=q) |
            Q(content__icontains=q) |
            Q(owner__username__icontains=q) |
            Q(category__title__icontains=q) |
            Q(tag__title__icontains=q)
        )
    # pagination
    page_number = request.GET.get("page")
    p = Paginator(blogs, 1)
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.get_page(1)
    except EmptyPage:
        page_obj = p.get_page(p.num_pages)
    context = {
        'blogs': blogs,
        'page_obj': page_obj,
    }
    return render(request, 'blog/blog.html', context)


def blog_detail(request, pk):
    blog = Blog.objects.get(id=pk)
    tags = Tag.objects.all()
    categories = Category.objects.all().annotate(blogs_count=Count('cat'))
    recent_blog = Blog.objects.all().order_by('-id')[:3]
    context = {
        'blog': blog,
        'tags': tags,
        'categories': categories,
        'recent_blog': recent_blog,
    }
    return render(request, 'blog/blog-single.html', context)


#



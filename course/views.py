from django.shortcuts import render
from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Course, Category, Tag


# Create your views here.
def courses(request):
    course_list = Course.objects.all()

    category = request.GET.get('category')
    if category:
        course_list = Course.objects.filter(category__title__exact=category)

    tag = request.GET.get('tag')
    if tag:
        course_list = Course.objects.filter(tag__title__exact=tag)

    q = request.GET.get('q')
    if q:
        course_list = Course.objects.distinct().filter(
            Q(title__icontains=q) |
            Q(content__icontains=q) |
            Q(owner__username__icontains=q) |
            Q(category__title__icontains=q) |
            Q(tag__title__icontains=q)
        )
    # pagination
    page_number = request.GET.get("page")
    p = Paginator(course_list, 2)
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.get_page(1)
    except EmptyPage:
        page_obj = p.get_page(p.num_pages)

    context = {
        'course_list': course_list,
        'page_obj': page_obj,
    }
    return render(request, 'course/course.html', context)


def course(request, pk):
    course_detail = Course.objects.get(id=pk)
    tags = Tag.objects.all()
    categories = Category.objects.all().annotate(blogs_count=Count('cat'))
    recent_course = Course.objects.all().order_by('-id')[:3]
    context = {
        "course_detail": course_detail,
        "tags": tags,
        "categories": categories,
        "recent_course": recent_course,
    }
    return render(request, 'course/course-single.html', context)
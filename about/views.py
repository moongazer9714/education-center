from django.shortcuts import render
from course.models import Course
from blog.models import Blog


def index(request):
    courses_list = Course.objects.all().order_by('-id')[:3]
    recent_blog = Blog.objects.all().order_by('-id')[:3]

    context = {
        "courses_list": courses_list,
        "recent_blog": recent_blog,
    }
    return render(request, 'about/index.html', context)


def about_us(request):
    return render(request, 'about/about.html')


#
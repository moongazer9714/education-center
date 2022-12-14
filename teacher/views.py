from django.shortcuts import render
from .models import Teacher
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def teacher_list(request):
    teachers = Teacher.objects.all()
    page_number = request.GET.get("page")
    p = Paginator(teachers, 4)
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.get_page(1)
    except EmptyPage:
        page_obj = p.get_page(p.num_pages)
    context = {
        "teachers": teachers,
        "page_obj": page_obj,
    }
    return render(request, 'teacher/instructor.html', context)


def teacher_detail(request, pk):
    teacher = Teacher.objects.get(id=pk)

    context = {
        "teacher": teacher
    }
    return render(request, 'teacher/instructor-details.html', context)

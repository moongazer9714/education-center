from django import template
from blog.models import Blog
from course.models import Course


register = template.Library()


@register.inclusion_tag('blog/recent_posts_tpl.html')
def get_recent_blogs():
    blogs = Blog.objects.order_by('-id')[:6]
    return {"blogs": blogs}


@register.inclusion_tag('blog/recent_courses_tpl.html')
def get_recent_courses():
    courses = Course.objects.order_by('-id')[:6]
    return {"courses": courses}

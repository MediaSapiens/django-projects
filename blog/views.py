from annoying.decorators import render_to
from blog.models import BlogPost


@render_to('blog/index.html')
def blog(request):
    blog_post = BlogPost.objects.filter(active=True)
    return {'blog_post': blog_post}


@render_to('blog/full_news.html')
def full_news(request, article_slug):
    blog_post = BlogPost.objects.get(slug=article_slug)
    return {'blog_post': blog_post}

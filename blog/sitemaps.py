from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from blog.models import Post
from django.urls import reverse

class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.pub_date
    
    def location(self, item):
        return reverse("blog:single", kwargs={"pid": item.id})
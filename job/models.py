from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.


JOB_TYPE=(
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
 )

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Job(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    job_type=models.CharField(max_length=20, choices=JOB_TYPE)
    description=models.TextField()
    responsibilities=models.TextField()
    qualifications=models.TextField()
    benefits=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.CharField(max_length=100)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='jobs')
    slug=models.SlugField(blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate slug from title if not already set
            self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)


    def __str__(self):
        return self.title
    

    
class Apply(models.Model):
    job=models.ForeignKey(Job, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    website=models.URLField(blank=True)
    cv=models.FileField(upload_to='apply/')
    cover_letter=models.TextField(blank=True)


    def __str__(self):
        return self.name

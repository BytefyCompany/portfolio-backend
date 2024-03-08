from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to="project_images")
    link = models.CharField(max_length=200)
    github_link = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
class About(models.Model):
    text = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
class ProgrammingLang(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    full_name = models.CharField(max_length=500)
    working_experience = models.CharField(max_length=100)
    programming_languages  = models.ManyToManyField(ProgrammingLang)

    def __str__(self):
        return self.full_name


class Contact(models.Model):
    full_name = models.CharField(max_length=500)
    message = models.TextField()
    number = models.PositiveIntegerField()
    email = models.EmailField()
    telegram_username = models.CharField(null=True, blank=True, max_length=100)
    is_accepted = models.BooleanField(default=False)



from django.db import models

from apps.base.models import BaseModel


class Project(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="projects", null=True, blank=True)
    is_seeking = models.BooleanField(default=True)
    owner = models.ForeignKey("oauth.User", on_delete=models.CASCADE)

    specialists = models.ManyToManyField("science.Specialist", related_name="projects")

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name


class ProjectImage(BaseModel):
    project = models.ForeignKey("science.Project", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="project_images")

    class Meta:
        verbose_name = "Project Image"
        verbose_name_plural = "Project Images"

    def __str__(self):
        return self.name


class Interest(BaseModel):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Interest"
        verbose_name_plural = "Interests"

    def __str__(self):
        return self.name


class Skill(BaseModel):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name


class Specialist(BaseModel):
    user = models.ForeignKey("oauth.User", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="specialists", null=True, blank=True)
    bio = models.TextField()

    interests = models.ManyToManyField("science.Interest", related_name="specialists")
    skills = models.ManyToManyField("science.Skill", related_name="specialists")

    class Meta:
        verbose_name = "Specialist"
        verbose_name_plural = "Specialists"

    def __str__(self):
        return self.user.username


class Vacancy(BaseModel):
    project = models.ForeignKey("science.Project", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_open = models.BooleanField(default=True)

    skills = models.ManyToManyField("science.Skill", related_name="vacancies")

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"

    def __str__(self):
        return self.name

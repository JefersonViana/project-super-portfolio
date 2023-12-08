from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    github = models.URLField(blank=False, max_length=500)
    linkedin = models.URLField(blank=False, max_length=500)
    bio = models.TextField(blank=False, max_length=500)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(blank=False, max_length=50)
    description = models.TextField(blank=False, max_length=500)
    github_url = models.URLField(blank=False, max_length=500)
    keyword = models.CharField(blank=False, max_length=50)
    key_skill = models.CharField(blank=False, max_length=50)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="projects",
    )

    def __str__(self):
        return self.name


# Crie um model Certificate
# Crie um model CertifyingInstitution
# Em uma única requisição, crie um certificado e uma instituição certificadora
# Associe o certificado à instituição certificadora


class CertifyingInstitution(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(blank=False, max_length=500)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(blank=False, max_length=100)
    certifying_institution = models.ForeignKey(
        CertifyingInstitution,
        on_delete=models.CASCADE,
        related_name="certificates",
        max_length=500,
        blank=False,
    )
    timestamp = models.DateTimeField(auto_now_add=True, blank=False)
    profiles = models.ManyToManyField(
        Profile,
        related_name="certificates",
        blank=False,
    )

    def __str__(self):
        return self.name

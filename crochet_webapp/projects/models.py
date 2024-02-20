from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

class Project(models.Model):
    name = models.CharField(max_length=128)
    completed = models.BooleanField(default=False)

class ProjectSection(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    section_name = models.CharField(max_length=128)
    row_count = models.IntegerField(default=0, validators=[MinValueValidator(0)])

class Yarn(models.Model):

    class YarnTypes(models.TextChoices):
        PLY1 = '1P', _('1 ply')
        PLY2 = '2P', _('2 ply')
        PLY4 = '4P', _('4 ply')
        DK = 'DK', _('Double Knitting')
        ARAN = 'AR', _('Aran')
        CHUNKY = 'CH', _('Chunky')
        SUPER_CHUNKY = 'SC', _('Super Chunky')

    brand = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=2, choices=YarnTypes, default=YarnTypes.DK)
    weight = models.IntegerField(default=100, validators=[MinValueValidator(0)])

class YarnColour(models.Model):
    yarn = models.ForeignKey(Yarn, on_delete=models.CASCADE)
    colour_id = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    colour_name = models.CharField(max_length=128, blank=True, null=True)
    num_skeins = models.IntegerField(validators=[MinValueValidator(0)])

class ProjectYarn(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    yarn = models.ForeignKey(YarnColour, on_delete=models.CASCADE)

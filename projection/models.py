from django.db import models
from authentication.models import User
from django.core.validators import FileExtensionValidator


class Proposal(models.Model):
    unique_code = models.CharField(unique=True, max_length=20)
    title = models.CharField(max_length=10)
    description = models.TextField(max_length=250)
    leader = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    members = models.ManyToManyField(User, related_name="member")
    file = models.FileField(upload_to='files', validators=[
                            FileExtensionValidator(['pdf'])])
    judges = models.ManyToManyField(User, related_name="judge")
    register_date = models.DateTimeField(auto_now_add=True)
    check_date = models.DateField(null=True)
    assent_date = models.DateField(null=True)
    present_date = models.DateField(null=True)
    accept_date = models.DateField(null=True)
    aontract_date = models.DateField(null=True)
    ip_address = models.CharField(max_length=15, null=True)

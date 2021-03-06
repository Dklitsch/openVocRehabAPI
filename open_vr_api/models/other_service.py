from django.db import models
from open_vr_api.models.service import Service


class OtherService(models.Model):

    transportation = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='transportation')

    maintenance = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='maintenance')

    Rehabilitation_technology = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='Rehabilitation_technology')

    personal_assistance_services = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='personal_assistance_services')

    technical_assistance_services = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='technical_assistance_services')

    reader_services = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='reader_services')

    interpreter_services = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='interpreter_services')

    other_services = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='other_services')

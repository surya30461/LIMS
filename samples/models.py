from django.db import models
from encrypted_model_fields.fields import EncryptedCharField

class Sample(models.Model):
    name = EncryptedCharField(max_length=100)  # Encrypt the name field
    sample_type = EncryptedCharField(max_length=50)  # Encrypt the sample_type field
    description = models.TextField(blank=True, null=True)  # Leave as is
    collected_on = models.DateTimeField(auto_now_add=True)  # Leave as is

    def __str__(self):
        return self.name

from typing import ClassVar

from django.db import models

from api.enums.DocumentType import DocumentType

from .User import User


class UserKYCInformation(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(
        User, related_name="kyc", on_delete=models.SET_NULL, null=True
    )
    bvn = models.CharField(max_length=20, null=True)
    document_type = models.CharField(
        max_length=30, choices=DocumentType.choices, null=True
    )
    document_id = models.CharField(max_length=255, null=True)
    is_bvn_verified = models.BooleanField(default=False, null=True)
    is_document_verified = models.BooleanField(default=False, null=True)
    created_at = models.DateField(auto_now_add=True)
    last_updated_at = models.DateField(auto_now=True)

    class Meta:
        indexes: ClassVar = [
            models.Index(fields=["is_bvn_verified"]),
            models.Index(fields=["is_document_verified"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["last_updated_at"]),
        ]

    def __str__(self) -> str:
        return str(self.id)

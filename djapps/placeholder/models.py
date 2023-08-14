from django.db import models

class UserInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.CharField(max_length=100)
    email = models.EmailField(max_length=120)
    address = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f"{self.id} {self.user}"
    
    def to_dict(self) -> dict:
        return dict(
            id=self.id,
            user=self.user,
            email=self.email,
            address=self.address
        )
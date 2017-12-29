from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Profile(models.Model):
    """User profile information definition."""

    # User relation
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Personal information
    birth_date = models.DateField(null=True)

    # Professional information
    linkedin_profile = models.URLField(null=True)

    def __str__(self):
        """Return a string representation of this object."""
        return self.user.get_full_name()


@receiver(post_save, sender=User)
def manage_user_profile(sender, instance, created, **kwargs):
    """Create or update user profile on user changes."""
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

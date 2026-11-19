from django.db.models.signals import pre_save, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from motorcycles.models import Motorcycle, MotorcycleInventory
from openai_api.client import get_motorcycle_ai_bio


def motorcycle_inventory_update():
    motorcycles_count = Motorcycle.objects.all().count()
    motorcycles_value = Motorcycle.objects.aggregate(
        total_value=Sum('value')
    )['total_value']
    MotorcycleInventory.objects.create(
        motorcycles_count = motorcycles_count,
        motorcycles_value = motorcycles_value
    )


@receiver(pre_save, sender=Motorcycle)
def motorcycle_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        ai_bio = get_motorcycle_ai_bio(
            instance.model, instance.brand, instance.model_year
        )
        instance.bio = ai_bio


@receiver(post_save, sender = Motorcycle)
def motorcycle_post_save(sender, instance, **kwargs):
        motorcycle_inventory_update()


@receiver(post_delete, sender = Motorcycle)
def motorcycle_post_delete(sender, instance, **kwargs):
    motorcycle_inventory_update()



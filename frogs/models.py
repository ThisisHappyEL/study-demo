from django.db import models

# Create your models here.
class FrogType(models.Model):
    """
    Видовая принадлежность лягухи. Содержит в себе информацию о:
    Содержит в себе информацию о названии вида и её рыночную стоимость
    """
    name = models.CharField(max_length=100, verbose_name="Название вида")
    default_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стандартная цена")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вид лягушки"
        verbose_name_plural = "Виды лягушек"

class FrogAquarium(models.Model):
    """
    Ёмкость с лягухами для продажи. Содержит в себе информацию о:
    Информацию о стоимости аквариума,
    """
    aquarium_size = models.CharField(max_length=50, default='10x10', verbose_name="Размер аквариума")
    aquarium_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Стоимость самого аквариума")

    @property
    def current_quantity(self):
        return self.frogs.count()

    @property
    def total_price(self):
        frogs_value = sum(frog.price for frog in self.frogs.all())
        return self.aquarium_price + frogs_value

    @property
    def stored_types_display(self):
        types = self.frogs.values_list('frog_type__name', flat=True).distinct()
        return ", ".join(types)

    def __str__(self):
        return f"Аквариум {self.id} ({self.aquarium_size})"

    class Meta:
        verbose_name = "Аквариум"
        verbose_name_plural = "Аквариумы"

class Frog(models.Model):
    """
    Конкретная лягуха. Содержит в себе информацию о:
    Видовая принадлежность лягухи,
    Аквариум, в котором она содержится
    Информацию о стоимости конкретной лягухи
    """
    frog_type = models.ForeignKey(FrogType, on_delete=models.CASCADE, verbose_name="Вид лягухи")
    aquarium = models.ForeignKey(FrogAquarium, on_delete=models.CASCADE, related_name='frogs', verbose_name="Аквариум")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена лягухи", blank=True)

    def save(self, *args, **kwargs):
        if self.price is None:
            self.price = self.frog_type.default_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.frog_type.name} в аквариуме {self.aquarium.id}"

    class Meta:
        verbose_name = "Лягушка"
        verbose_name_plural = "Лягушки"


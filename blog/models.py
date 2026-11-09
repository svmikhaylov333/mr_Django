from django.db import models


class BlogPost(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок",
        # help_text="Введите заголовок записи",
    )
    content = models.TextField(
        verbose_name="Содержимое",
        # help_text="Введите текст записи",
    )
    preview = models.ImageField(
        upload_to="blog/previews/",
        blank=True,
        null=True,
        verbose_name="Превью(изображение)",
        # help_text="Загрузите изображение для превью",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовать",
        # help_text="Отметьте, если запись опубликована",
    )
    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество просмотров",
    )

    class Meta:
        verbose_name = "Запись блога"
        verbose_name_plural = "Записи блога"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


# заголовок,
# содержимое,
# превью (изображение),
# дата создания,
# признак публикации (булевое поле),
# количество просмотров.

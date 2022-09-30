import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Genre(TimeStampedMixin, UUIDMixin):
    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "content\".\"genre"
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Filmwork(TimeStampedMixin, UUIDMixin):

    class TypeOfFilm(models.TextChoices):
        MOVIE = 'movie', _('movie')
        TV_SHOW = 'tv show', _('tv show')

    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    rating = models.FloatField(_('rating'), blank=True,
                               validators=[MinValueValidator(0),
                                           MaxValueValidator(100)])
    type = models.CharField(
                            _('type'),
                            max_length=50,
                            choices=TypeOfFilm.choices,
                            default=TypeOfFilm.MOVIE
                            )
    creation_date = models.DateField(_('creation date'))
    genres = models.ManyToManyField(Genre, through='GenreFilmwork')
    file_path = models.FileField(
                                _('file'),
                                blank=True,
                                null=True,
                                upload_to='movies/'
                                )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = 'Кинопроизведение'
        verbose_name_plural = 'Кинопроизведения'
        indexes = [
            models.Index(fields=['creation_date', 'rating'],
                         name='film_work_date_rating_idx'),
        ]


class GenreFilmwork(UUIDMixin):
    film_work = models.ForeignKey(Filmwork, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"genre_film_work"
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        constraints = [
            models.UniqueConstraint(fields=['film_work_id', 'genre_id'],
                                    name='film_work_genre_idx'),
        ]


class Person(TimeStampedMixin, UUIDMixin):

    full_name = models.TextField(_('full name'))

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "content\".\"person"
        verbose_name = 'Персона'
        verbose_name_plural = 'Персоны'


class PersonFilmwork(UUIDMixin):
    film_work = models.ForeignKey(Filmwork, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    class Role(models.TextChoices):
        DIRECTOR = 'director', _('Режисер')
        ACTOR = 'actor', _('Актер')
        WRITER = 'writer', _('Сценарист')

    role = models.CharField(choices=Role.choices, max_length=9)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"person_film_work"
        verbose_name = 'Персона'
        verbose_name_plural = 'Персоны'
        indexes = [
            models.Index(fields=['film_work_id', 'person_id'],
                         name='film_work_person_idx'),
        ]

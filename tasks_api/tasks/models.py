from django.db import models
from users.models import User

STATUS = (
    ('todo', 'todo'),
    ('in_progress', 'in_progress'),
    ('done', 'done'),
)


class Board(models.Model):
    """Модель доски."""

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Наименование'
    )


class Column(models.Model):
    """Модель колонки."""

    name = models.CharField(
        max_length=100,
        verbose_name='Наименование'
    )
    board = models.ForeignKey(
        Board,
        on_delete=models.CASCADE,
        verbose_name='Доска',
    )


class Sprint(models.Model):
    """Модель спринта."""

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Наименование'
    )
    start_date = models.DateTimeField(
        'Дата Старта',
    )
    end_date = models.DateTimeField(
        'Дата окончания',
    )


class Group(models.Model):
    """Модель группы."""

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Наименование'
    )


class Task(models.Model):
    """Модель задачи."""

    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )
    description = models.TextField('Описание')
    status = models.CharField(choices=STATUS, verbose_name='Статус')
    created_at = models.DateTimeField(
        'Дата создания', auto_now_add=True,
    )
    author_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='tasks_authors'
    )
    assignee_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Присвоено',
        related_name='tasks_assignee',
        blank=True,
        null=True
    )
    column_id = models.ForeignKey(
        Column,
        on_delete=models.CASCADE,
        verbose_name='Колонка',
        blank=True,
        null=True
    )
    sprint_id = models.ForeignKey(
        Sprint,
        on_delete=models.CASCADE,
        verbose_name='Спринт',
        blank=True,
        null=True
    )
    board_id = models.ForeignKey(
        Board,
        on_delete=models.CASCADE,
        verbose_name='Доска',
        blank=True,
        null=True
    )
    group_id = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name='Группа',
        blank=True,
        null=True
    )
    watchers = models.ManyToManyField(
        User,
        verbose_name='Наблюдатели',
        related_name='watched_tasks'
    )
    executors = models.ManyToManyField(
        User,
        verbose_name='Исполнители',
        related_name='executed_tasks'
    )

    class Meta:
        indexes = [
            models.Index(fields=['created_at']),
        ]

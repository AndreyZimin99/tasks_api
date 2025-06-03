from django_filters import rest_framework as filters
from rest_framework import mixins, viewsets
from rest_framework.pagination import PageNumberPagination
import logging


from api.serializers import TaskSerializer
from tasks.models import Task

logger = logging.getLogger('api')


class TaskViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = PageNumberPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = (
        'status',
        'author_id',
        'assignee_id',
        'board_id',
        'sprint_id',
    )

    def list(self, request, *args, **kwargs):
        logger.info('Запрос на получение списка задач')
        try:
            response = super().list(request, *args, **kwargs)
        except Exception as e:
            logging.error('Произошла ошибка: %s', e)
            raise
        logger.info(f'Количество задач: {len(response.data)}')
        return response

    def create(self, request, *args, **kwargs):
        logger.info('Запрос на создание новой задачи')
        try:
            response = super().create(request, *args, **kwargs)
        except Exception as e:
            logging.error('Произошла ошибка: %s', e)
            raise
        logger.info(f'Создана задача с ID: {response.data['id']}')
        return response

    def destroy(self, request, *args, **kwargs):
        logger.info(f'Запрос на удаление задачи с ID: {kwargs['pk']}')
        try:
            response = super().destroy(request, *args, **kwargs)
        except Exception as e:
            logging.error('Произошла ошибка: %s', e)
            raise
        logger.info(f'Задача с ID: {kwargs['pk']} успешно удалена')
        return response

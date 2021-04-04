from rest_framework import routers
from .views import TodoView

router = routers.DefaultRouter()
router.register('todo', TodoView, 'todo')

urlpatterns = router.urls

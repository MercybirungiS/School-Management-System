
from django.urls.conf import path,include
from rest_framework import routers, urlpatterns
from .views import CourseViewSet, EventViewSet, StudentViewSet,TrainerViewSet

router=routers.DefaultRouter()
router.register("students/",StudentViewSet)
router.register("trainers/",TrainerViewSet)
router.register("courses/",CourseViewSet)
router.register("events/",EventViewSet)

urlpatterns=[
    path("" ,include(router.urls)),
]
# from apscheduler.jobstores.base import JobLookupError
# from apscheduler.triggers.cron import CronTrigger
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from teprunner.models import Plan, PlanCase, Case, PlanResult
from teprunner.serializers import PlanSerializer, PlanCaseSerializer, PlanResultSerializer
from teprunner.views.run import run_plan_engine
from teprunner.views.task import scheduler
from user.pagination import CustomPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
import jenkins
from django.conf import settings

# server = jenkins.Jenkins('http://192.168.50.11:8028')
server = jenkins.Jenkins(settings.JENKINS_URL, username=settings.JENKINS_USER, password=settings.JENKINS_PASSWD)


@api_view(['GET'])
@permission_classes((AllowAny,))
@authentication_classes(())
def get_jobs(request):
    jobs = server.get_jobs()
    return Response({"data": jobs}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((AllowAny,))
@authentication_classes(())
def build_job(request):
    job_name = request.data.get("job_name")
    job_params = request.data.get("job_params")
    my_job = server.get_job_config(job_name)
    print(my_job) # prints XML configuration
    server.build_job(job_name,  job_params)
    return Response({"data": my_job}, status=status.HTTP_200_OK)

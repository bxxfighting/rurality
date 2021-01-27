from django.db import transaction
from django.db.models import Q

from business.service.models import ServiceModel
from business.service.models import ServiceAssetObjModel
from scheduler.models import ServiceBerryModel
from component.jenkins.controllers.server import get_jenkins_cli
from base import errors
from base import controllers as base_ctl


def publish_service(berry_obj):
    berry_obj = ServiceBerryModel.objects.filter(id=berry_obj.id).first()

    jenkins_cli = get_jenkins_cli()

    params = {
    }
    jenkins_cli.run_job(job_name, params)



from ..models.servicemodels import ServiceClientCall


class ServiceClientException(Exception):
    def __init__(self, serviceClientCall: ServiceClientCall):
        self._serviceClientCall = serviceClientCall

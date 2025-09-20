import logging
import http.client
import string

from ..models.servicemodels import Request, Response, ServiceClientCall, ServiceClientSettings
from .exceptions import ServiceClientException

class ServiceClient():
    def __init__(self, settings: ServiceClientSettings):
        self.logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}",
        )
        self.logger.info("ServiceClient initialized. BaseAddress: %s", settings.BaseAddress)
        self._settings = settings

    @property
    def ServiceClientSettings(self):
        return self._settings
        
    def POST(self, uri: string, request: Request) -> Response:
        requestBody = request.request.RequestModel.json()
        httpClient = http.client.HTTPConnection(self._settings.BaseAddress, self._settings.TimeoutInMilliseconds)
        httpClient.request("POST", uri, requestBody, headers=request.Headers)
        response = Response()
        try:
            rawResponse = httpClient.getresponse()
            response.ResponseModel = rawResponse.read()
            response.HttpStatus = rawResponse.status
            httpClient.close()
        except http.client.HTTPException as httpException:
            serviceClientCall = ServiceClientCall(request, response, httpException)
            raise ServiceClientException(serviceClientCall) from httpException

        return response

    def GET(self, uri: string, request: Request) -> Response:
        httpClient = http.client.HTTPConnection(self._settings.BaseAddress, self._settings.TimeoutInMilliseconds)
        httpClient.request("GET", uri, headers=request.Headers)
        response = Response()
        try:
            rawResponse = httpClient.getresponse()
            response.ResponseModel = rawResponse.read()
            response.HttpStatus = rawResponse.status
            httpClient.close()
        except http.client.HTTPException as httpException:
            serviceClientCall = ServiceClientCall(None, response, httpException)
            raise ServiceClientException(serviceClientCall) from httpException

        return response

import http.client
import string
from typing import TypeVar

TRequest = TypeVar('TRequest')


class Request():
    def __init__(self):
        pass

    @property
    def RequestModel(self):
        return self._requestModel

    @RequestModel.setter
    def RequestModel(self, value: TRequest):
        self._requestModel = value

    @property
    def Headers(self):
        return self._headers

    @Headers.setter
    def Headers(self, value: dict):
        self._headers = value

TResponse = TypeVar('TResponse')

class Response():
    def __init__(self):
        self._responseModel = None
        self._httpStatus = None

    @property
    def ResponseModel(self):
        return self._responseModel

    @ResponseModel.setter
    def ResponseModel(self, value: TResponse):
        self._responseModel = value

    @property
    def HttpStatus(self):
        return self._httpStatus

    @HttpStatus.setter
    def HttpStatus(self, value):
        self._httpStatus = value



class ServiceClientCall():
    def __init__(self, request, response, exception: http.client.HTTPException):
        self._request = request
        self._response = response
        self._exception = exception

    @property
    def Request(self):
        return self._request

    @property
    def Response(self):
        return self._response
    
    @property
    def Exception(self):
        return self._exception

class ServiceClientSettings():
    def __init__(self, baseAddress: string, timeoutInMilliseconds):
        self._baseAddress=baseAddress
        self._timeoutInMilliseconds = timeoutInMilliseconds

    @property
    def BaseAddress(self):
        return self._baseAddress

    @property
    def TimeoutInMilliseconds(self):
        return self._timeoutInMilliseconds
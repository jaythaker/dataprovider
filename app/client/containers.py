from dependency_injector import containers, providers

from .communicator import ServiceClient

class ServiceClientContainer(containers.DeclarativeContainer):

    configurations = providers.DependenciesContainer()

    serviceClient = providers.Singleton(ServiceClient, configurations.serviceClientSettings)
from dependency_injector import containers, providers

from ..models.servicemodels import ServiceClientSettings

class ConfigurationContainer(containers.DeclarativeContainer):

    clientConfiguration = providers.Configuration()

    serviceClientSettings = providers.Singleton(
        ServiceClientSettings, 
        clientConfiguration.settings.baseAddress, 
        clientConfiguration.settings.timeout
    )

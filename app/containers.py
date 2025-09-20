import logging.config

from dependency_injector import containers, providers

from .configuration.containers import ConfigurationContainer
from .client.containers import ServiceClientContainer
from .dataproviders.containers import DataProviderContainer
from .mapper.containers import MapperContainer

class Core(containers.DeclarativeContainer):

    config = providers.Configuration()

    logging = providers.Resource(
        logging.config.dictConfig,
        config=config.logging,
    )

class ApplicationContainer(containers.DeclarativeContainer):

    appConfiguration = providers.Configuration(yaml_files=["config.yml"]);

    core = providers.Container(
        Core,
        config=appConfiguration.core,
    )

    Configuration = providers.Container(ConfigurationContainer, clientConfiguration=appConfiguration.client)

    Client = providers.Container(ServiceClientContainer, configurations=Configuration)

    Mapper = providers.Container(MapperContainer)

    DataProvider = providers.Container(DataProviderContainer)

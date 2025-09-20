from dependency_injector import containers, providers
from ..services import authenticationservice as AuthenticationService

class Services(containers.DeclarativeContainer):

    config = providers.Configuration()
    # gateways = providers.DependenciesContainer()

    Authentication = providers.Factory(
        AuthenticationService
    )


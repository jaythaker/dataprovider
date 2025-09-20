"""Main module."""

import sys
import logging
from venv import logger


from dependency_injector.wiring import Provide, inject
from .client.communicator import ServiceClient
from .containers import ApplicationContainer

@inject
def main(
     service_client: ServiceClient = Provide[ApplicationContainer.Client.serviceClient]
    ) -> None:
    logger = logging.getLogger(__name__)


if __name__ == "__main__":
    application = ApplicationContainer()
    application.core.init_resources()
    application.wire(modules=[__name__])

    main(*sys.argv[1:])

from containers.factories.yaml import FactoryYaml
from helpers.containers.dependencyHelpers import *


class ApplicationContainer(containers.DeclarativeContainer):
    config = providers.Singleton(FactoryYaml.config)
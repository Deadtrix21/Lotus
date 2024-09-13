from bot.cluster.bot import DependencyBot
from containers.container import ApplicationContainer


def main() -> None:
    DependencyBot().run_bot()


if __name__ == "__main__":
    container = ApplicationContainer()
    container.init_resources()
    container.wire(modules=[__name__])
    main()

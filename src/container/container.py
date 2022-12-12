from dependency_injector import providers, containers

from src.database.database import Database
from src.database.repositories.item_repository import ItemRepository
from src.services.item_service import ItemService

# container is a collection of providers, which is Classes and Dependencies
class Container(containers.DeclarativeContainer):

    # provides a way to inject dependencies into the function and methods
    wiring_config = containers.WiringConfiguration(modules=["src.burger95s.api.items.item_controller"])    

    # creates Object of the Class only
    db = providers.Singleton(Database)

# creates an Object and Dependencies(the object depends on those Dependencies for initialization)
    # Repositories
    item_repository = providers.Factory(
        ItemRepository,
        session_factory=db.provided.session,
    )

    # Services
    item_service = providers.Factory(
        ItemService,
        item_repository=item_repository,
    )

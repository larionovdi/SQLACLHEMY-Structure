
from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Factory


from database.init_of_work import AlchemyUnitofWork
from users.database.repository import UserRepository
from database.session import Session


class Container(DeclarativeContainer):
    wiring_config = WiringConfiguration(
        packages=["users"]
    )

    session_creator = Factory(
        Session
    )

    users_repository = Factory(
        UserRepository,
        session = session_creator
    )
    users_uow = Factory(
        AlchemyUnitofWork,
        repository=users_repository
    )


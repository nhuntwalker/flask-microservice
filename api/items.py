"""A listing of all the items."""
from flask_injector import inject
from services.provider import ItemsProvider


@inject(data_provider=ItemsProvider)
def search(data_provider) -> list:
    """Return a list of items."""
    return data_provider.get()

"""."""
import connexion

from injector import Binder
from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver

from services.provider import ItemsProvider


def configure(binder: Binder) -> Binder:
    """Handle bindings to create the item container."""
    binder.bind(
        ItemsProvider,
        ItemsProvider([{"Name": "Test 1"}])
    )


if __name__ == "__main__":
    # create a new application and tell it what port we want to start on
    # define path to swagger configs
    app = connexion.App(__name__, 9090, specification_dir="swagger/")
    # add a new API (can have many); yaml file will define routes
    app.add_api("my_super_app.yaml", resolver=RestyResolver("api"))
    FlaskInjector(app=app.app, modules=[configure])
    app.run()

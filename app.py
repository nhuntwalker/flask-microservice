"""."""
from connexion.resolver import RestyResolver
import connexion


if __name__ == "__main__":
    # create a new application and tell it what port we want to start on
    # define path to swagger configs
    app = connexion.App(__name__, 9090, specification_dir="swagger/")
    # add a new API (can have many); yaml file will define routes
    app.add_api("my_super_app.yaml", resolver=RestyResolver("api"))
    app.run()

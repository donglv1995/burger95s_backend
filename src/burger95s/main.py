import argparse
import logging

from fastapi import FastAPI
from .api.items import item_controller
from .api.orders import order_controller
from .api.authen import authen_controller
from .api.burgers import burger_controller
from src.container.container import Container

from .version import __version__

logger = logging.getLogger(__package__)


# Init web-app API using FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:9999",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# create container and tables
container = Container()
db = container.db()
db.create_database()

# Init all routers within app
app.include_router(order_controller.router)
app.include_router(burger_controller.router)
app.include_router(item_controller.router)
app.include_router(authen_controller.router)




def main(args=None):
    """ Entry Point """
    argparser = argparse.ArgumentParser()
    args = argparser.parse_args(args)

    execute(args)

def execute(args): # pylint: disable=unused-argument
    """ Prints the package version """
    print(f'Burger95s_Backend v{__version__}')
    logger.info(f'Burger95s_Backend v{__version__}')

if __name__ == 'main':
    main()
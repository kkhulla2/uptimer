from sqlalchemy import create_engine
from sqlalchemy import text
from app import config
import logging

logger = logging.getLogger(__name__)

settings = config.Settings()
engine = create_engine(
    settings.database_url,
    connect_args={
        'connect_timeout': 2,
    },
    pool_pre_ping=True
    )


def get_health_check():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
    except Exception as e:
        logger.error(f'{e}')
        return False
    return True


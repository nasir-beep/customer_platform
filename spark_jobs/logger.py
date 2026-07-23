import logging
import os

os.makedirs("/opt/project/logs", exist_ok=True)

logging.basicConfig(
    filename="/opt/project/logs/spark_etl.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

logger = logging.getLogger(__name__)
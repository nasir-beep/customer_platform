import logging

def get_logger(name):
    """
    Create a reusable logger.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

    return logging.getLogger(name)
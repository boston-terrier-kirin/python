import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
                    filename="app.log")
logger = logging.getLogger("test_logger")

logger.info("This is info message")
logger.warning("This is warning message")

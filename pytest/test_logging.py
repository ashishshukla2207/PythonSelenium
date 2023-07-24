import logging

def test_logging():
    logger = logging.getLogger(__name__)

    filehandler = logging.FileHandler("logfile.log")

    formatter= logging.Formatter("%(asctime)s : %(levelname)s : %(name)s :%(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    logger.setLevel(logging.INFO)
    logger.debug("debug")
    logger.info("info")
    logger.warning("warn")
    logger.error("error")
    logger.critical("important")
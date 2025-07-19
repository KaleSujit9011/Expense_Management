import logging


def setup_logging(name,log_file, level=logging.INFO):
    # Create a custom logger
    logger = logging.getLogger(name)

    # Configure the custom logger
    logger.setLevel(level)

    # Use the provided log file name instead of a hardcoded value
    file_handler = logging.FileHandler(log_file)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger  # Ensure the function returns the logger


# Logging messages using the custom logger
# logger.debug("This is a debug message from my_logger")
# logger.info("This is an info message from my_logger")
# logger.warning("This is a warning message from my_logger")
# logger.error("This is an error message from my_logger")
# logger.critical("This is a critical message from my_logger")


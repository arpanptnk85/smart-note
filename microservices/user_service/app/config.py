import logging

logger = logging.Logger('user-service', logging.DEBUG)

file_handler = logging.FileHandler('./logs/user-service.log')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
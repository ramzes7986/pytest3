import logging

logging.basicConfig(
    filename='Api_tests.log',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger('my_logger')



logger = logging.getLogger(__name__)

# Настройка уровня логирования
logger.setLevel(logging.ERROR)

# Создание обработчика, который записывает логи в файл
handler = logging.FileHandler('error.log')

# Настройка уровня логирования для обработчика
handler.setLevel(logging.ERROR)

# Создание форматировщика сообщений лога
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Привязка форматировщика к обработчику
handler.setFormatter(formatter)

# Привязка обработчика к логгеру
logger.addHandler(handler)
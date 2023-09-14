from aiogram import executor
from Commands import dp
import logging
    
logger = logging.getLogger(__name__)
logging.basicConfig(filename="debug.log", filemode="w", level=logging.DEBUG, encoding='UTF-8', format='%(asctime)s - %(levelname)s - %(message)s', )

if __name__ =='__main__':
    executor.start_polling (dp, skip_updates=False)



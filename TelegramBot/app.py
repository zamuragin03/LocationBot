from aiogram import executor
from Commands import dp
from Commands.Tasks import CheckNotification
import logging
from Config import scheduler
    
logger = logging.getLogger(__name__)
logging.basicConfig(filename="debug.log", filemode="w", level=logging.DEBUG, encoding='UTF-8', format='%(asctime)s - %(levelname)s - %(message)s', )
async def on_startup(dispatcher):
    scheduler.start()
    CheckNotification()


if __name__ =='__main__':
    executor.start_polling (dp, on_startup=on_startup,skip_updates=False)



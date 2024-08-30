import logging
<<<<<<< HEAD
from config import dp, bot, admin
=======
import config
>>>>>>> a0a70cdcaed82690dce9a9effa7bcf03eaec6332
from aiogram.utils import executor
from handlers import commands, echo, game, FSM_reg, FSM_store, send_products, webapp, pin_message, admin_bot
from db import db_main

<<<<<<< HEAD
=======
admin = [1196009647]

>>>>>>> a0a70cdcaed82690dce9a9effa7bcf03eaec6332

async def on_startup(_):
    for i in admin:
        await config.bot.send_message(chat_id=i, text='Бот включен')
        await db_main.sql_create()


async def on_shutdown(_):
    for i in admin:
        await config.bot.send_message(chat_id=i, text='Бот выкдючен')


<<<<<<< HEAD
commands.register_commands(dp)
game.register_quiz(dp)
FSM_reg.register_fsm(dp)
FSM_store.store_fsm(dp)
send_products.register_send_products_handler(dp)
webapp.register_webapp(dp)
pin_message.register_pin(dp)
admin_bot.register_admin(dp)
echo.register_echo(dp)
=======
commands.register_commands(config.dp)
game.register_quiz(config.dp)
FSM_reg.register_fsm_store(config.dp)
FSM_store.store_fsm(config.dp)
send_products.register_send_products_handler(config.dp)
echo.register_echo(config.dp)
>>>>>>> a0a70cdcaed82690dce9a9effa7bcf03eaec6332


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(config.dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)

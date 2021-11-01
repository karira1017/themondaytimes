#init
#import pymysql
#pymysql.version_info = (1, 3, 13, "final", 0)
#pymysql.install_as_MySQLdb()
import sys
import asyncio

if sys.platform == "win32" and sys.version_info >= (3, 8, 0):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
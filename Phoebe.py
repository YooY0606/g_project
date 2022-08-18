
from app import app
import logging

if __name__ == "__main__":
    # app.debug = True
    handler_log = logging.FileHandler('flask.log', encoding='UTF-8')
    handler_log.setLevel(
        logging.DEBUG
    )  # 設定日誌記錄最低級別為DEBUG，低於DEBUG級別的日誌記錄會被忽略，不設定setLevel()則預設為NOTSET級別。
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s'
    )
    handler_log.setFormatter(logging_format)
    app.logger.addHandler(handler_log)

    # crawler()
    # read_db()
    app.run()
    # app.run(host='0.0.0.0',port='5020',debug=True)
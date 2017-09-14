"""
WSGI config for animeapi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import time
#import api.resident こいつインポートするとバグる
import threading

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "animeapi.settings")

application = get_wsgi_application()



import api.resident as logger #[重要]アプリケーション起動後にimport

#t = threading.Thread(target=logger.process) #スクレイピングの定期実行
#t.start()

logger.process()

p = threading.Thread(target=logger.awake) #サーバーへの定期アクセス
p.start()




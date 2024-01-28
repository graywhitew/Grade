import logging

from core.models import Log

class LoggingHandler(logging.Handler):
    """Сохраняет лог сообщений в MongoDB."""

    def emit(self, record):
        Log.objects.create(
            user = 'Sergey',
            additional_info={
                'module': record.module,
                'process': record.process,
                'msecs': record.msecs
            },
            message=self.format(record),
        )

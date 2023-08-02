from datetime import datetime
import humanize


class Util():


    @classmethod
    def convert_moment_human(self, date: datetime) -> str:
        return humanize.naturaldelta(datetime.now() - date)

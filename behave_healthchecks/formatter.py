import re

from behave.formatter.base import Formatter
from healthchecks_io import Client


CHECKS_CLIENT = Client(ping_url="localhost:1234")


class HealthCheckFormatter(Formatter):

    def __init__(self, stream_opener, config):
        super().__init__(stream_opener, config)
        self.current_scenario = None

    @staticmethod
    def get_health_check_for_scenario(tag: str) -> str or None:
        match = re.match(r"^healthcheck\('(.+)'\)$", tag, flags=re.IGNORECASE)
        if match:
            return match.group(1)
        else:
            return None

    @staticmethod
    def extract_health_check_id_from_tags(tags: list) -> str or None:
        for tag in tags:
            check_id = HealthCheckFormatter.get_health_check_for_scenario(tag)
            if check_id is not None:
                return check_id
        return None

    def scenario(self, scenario):
        self.current_scenario = scenario
        print (scenario.tags)
        check_id = self.extract_health_check_id_from_tags(scenario.tags)
        if check_id is not None:
            CHECKS_CLIENT.start_ping(uuid=check_id)
        print ("check: " + self.extract_health_check_from_tags(scenario.tags))
        pass

    def result(self, step):
        print (step)
        pass

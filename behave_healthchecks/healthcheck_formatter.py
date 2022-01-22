import os
import re

from behave.model import Scenario
from healthchecks_io import Client

from behave_healthchecks.better_formatter import BetterFormatter

PING_URL = os.environ.get("PING_URL", "https://hc-ping.com/")
CHECKS_CLIENT = Client(ping_url=PING_URL)


class HealthCheckFormatter(BetterFormatter):

    def __init__(self, stream_opener, config):
        super().__init__(stream_opener, config)
        self.scenario_check_ids = {}

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

    def scenario(self, scenario: Scenario):
        super().scenario(scenario)
        check_id = self.extract_health_check_id_from_tags(scenario.tags)
        self.scenario_check_ids[scenario.name] = check_id
        if check_id is not None:
            CHECKS_CLIENT.start_ping(uuid=check_id)

    def _check_id_for_scenario(self, scenario: Scenario):
        return self.scenario_check_ids[scenario.name]

    def _do_if_check_id_for_scenario(self, do: callable, scenario: Scenario):
        check_id = self._check_id_for_scenario(scenario)
        if check_id is not None:
            do(check_id)

    def scenario_success(self, scenario: Scenario):
        self._do_if_check_id_for_scenario(lambda check_id: CHECKS_CLIENT.success_ping(uuid=check_id), scenario)

    def scenario_failed(self, scenario: Scenario):
        self._do_if_check_id_for_scenario(lambda check_id: CHECKS_CLIENT.fail_ping(uuid=check_id), scenario)

    def scenario_skipped(self, scenario: Scenario):
        pass

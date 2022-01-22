import logging

from behave.formatter.base import Formatter
from behave.model import Scenario
from behave.model_core import Status


class BetterFormatter(Formatter):

    def __init__(self, stream_opener, config):
        super().__init__(stream_opener, config)
        self.current_scenario = None
        self.scenario_results = {}

    def scenario(self, scenario):
        self.current_scenario = scenario

    def result(self, step):
        if self.current_scenario.status == Status.untested:
            return
        self._append_scenario_result(step.status)

    def eof(self):
        for scenario in self.scenario_results.keys():
            logging.info(f"Finalising scenario with name [ {scenario.name} ]")
            self._finalise_scenario(scenario)

    def scenario_success(self, scenario: Scenario):
        raise NotImplementedError()

    def scenario_failed(self, scenario: Scenario):
        raise NotImplementedError()

    def scenario_skipped(self, scenario: Scenario):
        raise NotImplementedError()

    def _append_scenario_result(self, result: Status):
        logging.warning("Appending result " + str(result))
        if self.current_scenario in self.scenario_results:
            self.scenario_results[self.current_scenario].append(result)
        else:
            self.scenario_results[self.current_scenario] = [result]

    def _finalise_scenario(self, scenario: Scenario):
        results = self.scenario_results[scenario]

        at_least_one_success = False
        for result in results:
            if result == Status.failed or result == Status.undefined:
                logging.warning("Scenario failed!")
                self.scenario_failed(scenario)
                return
            elif result == Status.passed:
                at_least_one_success = True

        if at_least_one_success:
            logging.warning("Scenario success!")
            self.scenario_success(scenario)
        else:
            logging.warning("Scenario skipped!")
            self.scenario_skipped(scenario)

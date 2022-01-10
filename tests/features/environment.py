from behave import use_fixture

from tests.features.fixtures import start_mock_server


def before_tag(context, tag):
    if tag == "fixture.mock_healthchecks":
        use_fixture(start_mock_server, context, timeout=10)

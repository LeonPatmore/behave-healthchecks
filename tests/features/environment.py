from behave import use_fixture

from tests.features.fixtures import start_mock_server


_MOCK_HEALTH_CHECKS_IO_TAG_NAME = "fixture.mock_health_checks_io"


def before_tag(context, tag):
    if tag == _MOCK_HEALTH_CHECKS_IO_TAG_NAME:
        use_fixture(start_mock_server, context, timeout=10)

from behave import fixture
from ..test import main


@fixture
def start_mock_server(context, **kwargs):
    main()

from behave import given, when, then


@given('I am a test')
def i_am_a_user(context):
    pass


@when('I run')
def i_send_a_request(context):
    pass


@then('Ping was started')
def check_ping_started(context):
    context.mock_server.ping_started()


@then('Nothing')
def nothing(context):
    pass

from behave import given, when, then


@given('I am a test')
def i_am_a_user(context):
    pass


@when('I run')
def i_send_a_request(context):
    pass


@then('Success')
def success(context):
    pass


@then('Failure')
def failure(context):
    assert 1 == 2

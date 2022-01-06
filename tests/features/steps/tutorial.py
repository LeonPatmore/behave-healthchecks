from behave import given, when, then



@given('I am a user')
def i_am_a_user(context):
    pass


@when('I send a request')
def i_send_a_request(context):
    pass


@then('I get a response')
def i_get_a_response(context):
    assert 1 == 1

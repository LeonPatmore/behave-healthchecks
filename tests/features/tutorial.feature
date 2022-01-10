Feature: A test feature

  @healthcheck('abc123')
  @fixture.
  Scenario: run a test
    Given I am a user
    When I send a request
    Then I get a response

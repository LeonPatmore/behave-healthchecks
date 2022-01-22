@fixture.mock_health_checks_io
Feature: A test feature

  @healthcheck('abc123')
  Scenario: Sends start ping
    Given I am a test
    When I run
    Then Ping was started

  Scenario: Without healhcheck works
    Given I am a test
    When I run
    Then Nothing

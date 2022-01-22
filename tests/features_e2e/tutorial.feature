Feature: Testing healthchecks

  @healthcheck('5aa8ffc9-7440-4659-a9f0-11616b336348')
  Scenario: Success
    Given I am a test
    When I run
    Then Success

  @healthcheck('8b1d0640-ff62-4056-87bb-a7daf1929dc7')
  Scenario: Failure
    Given I am a test
    When I run
    Then Failure

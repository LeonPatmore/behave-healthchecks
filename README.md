# Behave Healthchecks

A Healthcheck io plugin for the Behave testing library. 

- https://healthchecks.io
- https://behave.readthedocs.io/en/stable/

Automatically sends the following signals to Healthcheck io based on the output of 
a scenario:

- Started
- Success
- Failure

## Installation

TODO

## Usage

In your behave feature file, add the following tag:

```gherkin
@healthcheck('<check_id>')
```

When you run behave, you must run with our formatter. For example:

`behave -f behave_healthchecks:HealthCheckFormatter`

## Example

```gherkin
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
```

## Testing

For unit tests:

`make test`

For e2e tests:

`make teste2e`

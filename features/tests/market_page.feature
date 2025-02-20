# Created by laris at 1/14/2025
Feature: Market Page Tests

  Scenario: User can open market tab and go through the pagination
#    Given Open Reelly page
#    When Log in to the page
#    And Click on “market” at the left side menu
#    Then Verify the Market page opens
#    When Go to the final page using pagination
    When Go to the first page using pagination

  Scenario: User can open market tab and filter by developers option
    Given Open Reelly page
    When Log in to the page
    And Click on “market” at the left side menu
    Then Verify the Market page opens
    When Click on Developers filter at the top of the page
    Then Verify all cards have the license tag

  Scenario: User can open market tab and add company option
    Given Open Reelly page
    When Log in to the page
    And Click on “market” at the left side menu
    Then Verify the Market page opens
    When Click on “Add company” button
    Then Verify the "Add company" page opens
    Then Verify the button “Publish my company” is available


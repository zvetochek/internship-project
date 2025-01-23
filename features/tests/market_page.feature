# Created by laris at 1/14/2025
Feature: Market Page Tests

  Scenario: User can open market tab and go through the pagination
    Given Open Reelly page
    When Log in to the page
    And Click on “market” at the left side menu
    Then Verify the Market page opens
    When Go to the final page using pagination
    When Go to the first page using pagination

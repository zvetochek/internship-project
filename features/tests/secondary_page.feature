# Created by laris at 2/4/2025
Feature: Tests for Secondary page

  Scenario: User can filter the Secondary deals by Unit price range,16
    Given Open Reelly page
    When Log in to the page
    When Click on “Secondary” option at the left side menu
    Then Verify the secondary page opens
    When Click on Filters
    When Filter products by price range from 1200000 to 2000000 AED
    Then Verify prices in all cards is in a given range
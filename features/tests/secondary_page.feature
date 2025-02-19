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

  Scenario:  User can open the Secondary deals page and go through the pagination, 13
    Given Open Reelly page
    When Log in to the page
    When Click on “Secondary” option at the left side menu
    Then Verify the secondary page opens
    When Go to the final secondary page using the pagination button
    When Go back to the first secondary page using the pagination button

  Scenario: User can filter the Secondary deals by “want to sell” 14
    Given Open Reelly page
    When Log in to the page
    When Click on “Secondary” option at the left side menu
    Then Verify the secondary page opens
    When Click on Filters
    And Filter the products by "want to sell"
    And Click on Apply Filter
    Then Verify all cards have "for sale" tag

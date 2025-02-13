# Created by laris at 12/5/2024
Feature: Tests for Off-plan page

  Scenario: User can filter the off plan products by Unit price range
   Given Open Reelly page
   When Log in to the page
   When Click on “off plan” at the left side menu
   Then Verify the right off-plan page opens
   When Filter the products by price range from 1200000 to 2000000 AED
   Then Verify the price in all cards is in a given range

 Scenario: User can filter by sale status Out of Stocks
    Given Open Reelly page
    When Log in to the page
    When Click on “off plan” at the left side menu
    Then Verify the right off-plan page opens
    When Filter by sale status of “Out of Stocks”
    Then Verify each product contains the Out of Stocks tag

 Scenario: User can open product detail and see three options of visualization
   Given Open Reelly page
   When Log in to the page
   And Click on “off plan” at the left side menu
   And Click on the first product
   Then Verify the three options of visualization are “architecture”, “interior”, “lobby”
   And Verify the visualization options are clickable

 Scenario: User can see titles and pictures on each product inside the off plan page
   Given Open Reelly page
   When Log in to the page
   When Click on “off plan” at the left side menu
   Then Verify the right off-plan page opens
   Then Verify each product on this page contains a title and picture visible

 Scenario: User can open the off plan page and go through the pagination, 17
   Given Open Reelly page
   When Log in to the page
   When Click on “off plan” at the left side menu
   Then Verify the right off-plan page opens
   When Go to the final page using the pagination button
   When Go back to the first page using the pagination button


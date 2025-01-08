# Created by laris at 12/5/2024
Feature: Off plan products tests
  # Enter feature description here

  Scenario: User can filter the off plan products by Unit price range
   Given Open Reelly page
   When Log in to the page
   When Click on “off plan” at the left side menu
   Then Verify the right off-plan page opens
   When Filter the products by price range from 1200000 to 2000000 AED
   Then Verify the price in all cards is in a given range
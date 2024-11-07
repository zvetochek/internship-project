Feature: User can navigate Settings option


  Scenario: User can open Subscription & payments page
    Given Open Reelly page
    When Enter email and password
    And Click on Continue button
    And Click on settings option
    And Click on Subscription & payments option
    Then Verify the right page opens
    Then Verify title “Subscription & payments” is visible
    Then Verify “back” and “upgrade plan” buttons are available




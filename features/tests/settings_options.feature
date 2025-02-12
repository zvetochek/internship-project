Feature: Tests for Settings options


  Scenario: User can open Subscription & payments page
    Given Open Reelly page
    When Log in to the page
    And Click on settings option
    And Click on Subscription & payments option
    Then Verify the right page opens
    Then Verify title “Subscription & payments” is visible
    Then Verify “back” and “upgrade plan” buttons are available

#  Scenario: User can open Subscription & payments page on Mobile
#    Given Open Reelly page
#    When Log in to the page
#    And Click on Main Menu
#    And Click on profile icon
#    And Click on Subscription & payments option
#    Then Verify the right page opens
#    Then Verify title “Subscription & payments” is visible
#    Then Verify “back” and “upgrade plan” buttons are available

  Scenario: 24 User can click on verifications settings option
    Given Open Reelly page
    When Log in to the page
    And Click on settings option
    And Click on the verification option
    Then Verify the verification page opens
    Then Verify “upload image” and “Next step” buttons are available

  Scenario: 2 The user can click on “Connect the company” on the left side of the main page
    Given Open Reelly page
    When Log in to the page
    And Click on settings option
    When Click on “Connect the company”
    And Switch the new tab
    Then Verify the right tab opens

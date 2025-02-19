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

  Scenario: User can go to settings and edit the personal information, 3
    Given Open Reelly page
    When Log in to the page
    And Click on settings option
    And Click on Edit profile option
    When Enter test information in the input fields
    Then Check the right information is present in the input fields
    Then Check “Close” and “Save Changes” buttons are available and clickable

  Scenario: User can change the language from the page, 4
    Given Open Reelly page
    When Log in to the page
    And Click on settings option
    And Change the language of the page to Russian. The option will be “RU” which is the list of the languages
    Then Verify the language has changed

  Scenario: User can add a project through the settings, 5
    Given Open Reelly page
    When Log in to the page
    And Click on settings option
    And Click on "Add a project" button
    Then Verify the "Add a project" page opens
    When Add some test information to the input fields
    Then Verify the right information is present in the input fields
    Then Verify “Send an application” button is available and clickable

  Scenario: User can open the community page, 6
    Given Open Reelly page
    When Log in to the page
    And Click on settings option
    When Click on Community option
    Then Verify the Community page opens
    Then Verify “Contact support” button is available and clickable

  Scenario: User can open the Contact us page, 7
    Given Open Reelly page
    When Log in to the page
    And Click on settings option
    And Click on "Contact us" option
    Then Verify the "Contact us" page opens
    Then Verify there are at least 4 social media icons
    Then Verify “Connect the company” button is available and clickable

  Scenario: User can open User guide page, 8
    Given Open Reelly page
    When Log in to the page
    And Click on settings option
    And Click on User Guide option
    Then Verify the User Guide page opens
    Then Verify all lesson videos contain titles

  Scenario: User can open change password page, 9
    Given Open Reelly page
    When Log in to the page
    And Click on settings option
    When Click on Change password option
    Then Verify Change password page opens
    When Add some test password to the input fields
    Then Verify the “Change password” button is available, but don’t click on it

  Scenario: User can access Whatsapp and Telegram communities, 11
    Given Open Reelly page
    When Log in to the page
    And Click on settings option
    And Click on support option
    And Switch to the new tab
    Then Verify the right page support opens
    When Go back
    When Click on news option
    Then Verify the news page opens
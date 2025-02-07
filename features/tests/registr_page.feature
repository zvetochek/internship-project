# Created by laris at 2/6/2025
Feature: Test for Registration page

  Scenario: 1 The user can enter the information into the input fields on the registration page
    Given Open the registration or sign up page
    When Enter some test information in the input fields
    Then Verify the right information is present
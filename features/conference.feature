Feature: Conference App Feature

  @conference
  Scenario: Verify Banner Appearance
    Given I launch the conference app
    When I skip the tutorial
    When I click on the about tab
    When I click on the location option
    When I select any other location value
    Then I should see the banner change
    When I switch to any other tab
    When I go back to the about tab
    Then I should see that banner has not changed

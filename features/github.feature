Feature: GitHub Login

  @github
  Scenario: User can navigate to GitHub sign in page
    Given I open the GitHub page
    When I click on sign in
    When I enter the credentials
    When I create a repository
    When I open repository settings
    When I try to delete repository
    Then I see the confirmation popup

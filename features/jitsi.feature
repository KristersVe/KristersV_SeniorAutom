Feature: Video call

  @jitsi
  Scenario: Desktop and mobile user video call
    Given I open the Jitsi meet app
    When I enter the room name
    When I enter my name and join the meeting
    When I login as moderator from mobile
    Then I verify video feeds for both devices

Feature: click
  In order to test runner's click method
  As a tester
  I will test the main click method

  Scenario: Test Runner.click method
    Given url "https://en.wikipedia.org/wiki/Main_Page"
    When I click the "Help" link
    Then I get the page entitled "Help:Contents - Wikipedia"

  Scenario: Test the Runner.click_link_text method
    Given url "https://en.wikipedia.org/wiki/Main_Page"
    When I call the click_link_text method to go to the "About Wikipedia" link
    Then I get the page entitled "Wikipedia:About - Wikipedia"

  Scenario: Test the Runner.click_anchor_tag_href method
    Given url "https://en.wikipedia.org/wiki/Main_Page"
    When I call the click_anchor_tag_href method with href "//en.wikipedia.org/wiki/Wikipedia:Contact_us"
    Then I get the page entitled "Wikipedia:Contact us - Wikipedia"

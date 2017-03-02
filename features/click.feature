"""
Copyright 2017 Raul Alvarez

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
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

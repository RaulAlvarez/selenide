from behave import *
from selenium.webdriver.common.by import By

from selenium.webdriver.support.expected_conditions import staleness_of

use_step_matcher("parse")

@given('url "{url}"')
def step_impl(context, url):
    context.url = url
    context.runner.browser.get(url)
    assert 'Wikipedia, the free encyclopedia' == context.runner.browser.title
    context.old_page = context.runner.browser.find_element_by_tag_name('html')

@when('I click the "{link}" link')
def step_impl(context, link):
    context.runner.click((By.LINK_TEXT, link))
    context.runner.wait.until(staleness_of(context.old_page))

@when('I call the click_link_text method to go to the "{link_text}" link')
def step_impl(context, link_text):
    context.runner.click_link_text(link_text)
    context.runner.wait.until(staleness_of(context.old_page))

@when('I call the click_anchor_tag_href method with href "{href}"')
def step_impl(context, href):
    context.runner.click_anchor_tag_href(href)
    context.runner.wait.until(staleness_of(context.old_page))

@then('I get the page entitled "{title}"')
def step_impl(context, title):
    assert title == context.runner.browser.title

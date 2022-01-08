import time
import environment
import asyncio
from playwright.sync_api import sync_playwright

from features.environment import before_all

@given('a Browser session is active')
def initiate_browser(context):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context.page = browser.new_page()
        context.page.goto('https://google.com')

@when('visit url "{url}"')
def visit_page(context, url):
    #this does not work ..event loop closed error
    context.page.goto('https://example.com')
    pass
    
    

'''@when('field with name "{selector}" is given "{value}"')
def step(context, selector, value):
    elem = context.browser.find_element_by_name(selector)
    elem.send_keys(value)
    elem.submit()
    time.sleep(5)

@then('title becomes "{title}"')
def step(context, title):
    assert context.browser.title == title

@then(u'page contains "{body}"')
def step(context, body):
    assert body in context.browser.page_source'''

import time
import environment
import asyncio
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
from behave import step
from behave.api.async_step import async_run_until_complete
from playwright.async_api import async_playwright

from features.environment import before_feature

@step('fire up the browser')
@async_run_until_complete
async def initiate_browser(context):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False,slow_mo=3000)
        page = await browser.new_page()
        #return(page)
        #page.goto('https://wikipedia.org')
        

@async_run_until_complete
@when('visit url "{url}"')
def step(context, url):
    #initiate_browser(context)
    #this does not work ..event loop closed error
    p = initiate_browser(context)
    p.goto(url)
    #pass
    
    
    

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

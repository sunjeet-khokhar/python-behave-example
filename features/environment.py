from selenium import webdriver
import os, json
from playwright.sync_api import sync_playwright


def before_all(context):
    pass

def before_feature(context, feature):
    pass
    
        
    '''desired_capabilities = CONFIG['environments'][TASK_ID]

    for key in CONFIG["capabilities"]:
        if key not in desired_capabilities:
            desired_capabilities[key] = CONFIG["capabilities"][key]

    context.browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="https://%s:%s@hub.testingbot.com/wd/hub" % (TB_KEY, TB_SECRET)
    )'''

def after_feature(context, feature):
    '''context.browser.quit()'''
    pass

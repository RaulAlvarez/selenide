import Selenium

def before_all(context):
    runner = Selenium.Selenium()
    context.runner = runner

def after_all(context):
    context.runner.quit()

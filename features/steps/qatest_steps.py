from behave import given, then, when
from test_data import *
from features.pages.home_page import QaTestHome


@given('User opens the app')
def step_impl(context):
    context.browser.get('https://qa-task.netlify.app/')


@when('User types existing command "{command}"')
def step_impl(context, command):
    page = QaTestHome(context)
    page.command_input.send_keys(command)
    page.execute_button.click()


@then('User sees the result "{result}"')
def step_impl(context, result):
    page = QaTestHome(context)
    result_text = ''.join(page.output_window.text.splitlines())
    assert result_text == result


@when('User types wrong command "{command}"')
def step_impl(context, command):
    page = QaTestHome(context)
    page.command_input.send_keys(command)
    page.execute_button.click()


@then('User sees not existing error')
def step_impl(context):
    page = QaTestHome(context)
    result_text = page.output_window.text
    assert result_text == wrong_command_output


@when('User does not type a command')
def step_impl(context):
    page = QaTestHome(context)
    page.execute_button.click()


@then('User sees empty error')
def step_imp(context):
    page = QaTestHome(context)
    result_text = page.output_window.text
    assert result_text == empty_command_output


@when('User types echo "{command}"')
def step_impl(context, command):
    page = QaTestHome(context)
    page.command_input.send_keys(command)
    page.execute_button.click()


@then('User sees the echo "{result}"')
def step_imp(context, result):
    page = QaTestHome(context)
    result_text = page.output_window.text
    assert result_text == result

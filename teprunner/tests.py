# from django.test import TestCase
from playwright.sync_api import Page
from playwright.sync_api import Playwright, sync_playwright, expect

# def test_visit_home_page(page: Page):
#     page.goto("https://reta-inc.com/")
#     page.get_by_text("功能介绍").click()
#     page.locator("span:has-text(\"用户评价\")").click()
#     page.locator("span:has-text(\"用户评价\")").click()
#     page.locator("span:has-text(\"应用下载\")").click()
#     page.get_by_placeholder("请输入手机号").click()
#     page.get_by_placeholder("请输入手机号").fill("1414213")
#     page.locator("div:nth-child(2) > .el-input > .el-input__wrapper").click()
#     page.get_by_placeholder("请输入验证码").fill("312321312")
#     page.get_by_role("button", name="马上注册").click()
def loginAdmin(page,ticket) -> None:
    admin='obj-{"id":16,"username":"conglin","email":"conglin@reta-inc.com","mobile":"123","status":0,"roleId":1,"role":{"id":1,"name":"admin","remark":null,"createdBy":null,"createdAt":1664321323000,"modifiedBy":null,"modifiedAt":1664321323000},"customer":null}'
    page.evaluate(f"""
                    document.cookie = "ticket={ticket};domain=.minnov.se;path=/"
                    localStorage.setItem('_user_','{admin}');
                  """)

def test_create_account(page: Page) -> None:

    page.goto("http://qa-e.minnov.se/login")
    # 管理员
    ticket = "82adfb5e-4ea7-43b0-938e-27f9c59f92b2"
    loginAdmin(page, ticket)
    page.goto("http://dev.e.minnov.se:8888/organization/account")

    page.get_by_role("button", name="Create Account").click()

    page.locator("input[name=\"username\"]").click()

    page.locator("input[name=\"username\"]").fill("test")

    page.get_by_role("dialog", name="Create Account").get_by_role("textbox", name="Please select").click()

    page.locator("#el-popper-container-5558").get_by_role("list").get_by_text("customer").click()

    page.get_by_placeholder("Please select or fill in").click()

    page.locator("li:has-text(\"Beijing FESCO Ent Service Group Co\")").click()

    page.locator("label:has-text(\"Inactive\") span").first.click()

    page.get_by_text("Active").nth(2).click()

    page.locator("input[name=\"mobile\"]").click()

    page.locator("input[name=\"mobile\"]").fill("13810264240")

    page.locator("input[name=\"email\"]").click()

    page.locator("input[name=\"email\"]").fill("email@fdaf.com")

    page.locator("input[name=\"password\"]").click()

    page.locator("input[name=\"password\"]").fill("123213123")

    page.get_by_role("button", name="Save").click()

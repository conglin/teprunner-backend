# from django.test import TestCase
from playwright.sync_api import Page
from playwright.sync_api import Playwright, sync_playwright, expect

def test_visit_home_page(page: Page):
    page.goto("https://reta-inc.com/")

    page.get_by_text("功能介绍").click()

    page.locator("span:has-text(\"用户评价\")").click()

    page.get_by_role("menuitem", name="功能介绍").click()

    page.locator("span:has-text(\"应用下载\")").click()

    page.locator("span:has-text(\"用户评价\")").click()

    page.locator("span:has-text(\"应用下载\")").click()

    page.get_by_placeholder("请输入验证码").click()

    page.get_by_placeholder("请输入验证码").fill("1245")

    page.get_by_placeholder("请输入手机号").click()

    page.get_by_placeholder("请输入手机号").fill("223232")

    # ---------------------
    # context.close()
    # browser.close()

# def run(playwright: Playwright) -> None:
#     # browser = playwright.chromium.launch(headless=False)
#     # context = browser.new_context()

#     page = context.new_page()

#     page.goto("https://reta-inc.com/")

#     page.get_by_text("功能介绍").click()

#     page.locator("span:has-text(\"用户评价\")").click()

#     page.get_by_role("menuitem", name="功能介绍").click()

#     page.locator("span:has-text(\"应用下载\")").click()

#     page.locator("span:has-text(\"用户评价\")").click()

#     page.locator("span:has-text(\"应用下载\")").click()

#     page.get_by_placeholder("请输入验证码").click()

#     page.get_by_placeholder("请输入验证码").fill("1245")

#     page.get_by_placeholder("请输入手机号").click()

#     page.get_by_placeholder("请输入手机号").fill("223232")

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)


# # Create your tests here.
# import jmespath
# from loguru import logger

# from tep.client import request
# import requests


# def test_post(faker_ch, env_vars, login):
#     # 描述
#     logger.info("test post")
#     # 数据
#     #fake = faker_ch
#     # 请求

#     cookies = {
#         'p_h5_u': 'B0B5C5A2-81CF-4FE4-8323-841C0B572EDA',
#         'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2241%22%2C%22first_id%22%3A%2217e9963bdb8ae3-093e3a033b10ed-133a6253-2073600-17e9963bdb957f%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfbG9naW5faWQiOiI0MSIsIiRpZGVudGl0eV9jb29raWVfaWQiOiIxN2U5OTYzYmRiOGFlMy0wOTNlM2EwMzNiMTBlZC0xMzNhNjI1My0yMDczNjAwLTE3ZTk5NjNiZGI5NTdmIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2241%22%7D%2C%22%24device_id%22%3A%2217e9963bdb8ae3-093e3a033b10ed-133a6253-2073600-17e9963bdb957f%22%7D',
#     }

#     headers = {
#         'Connection': 'keep-alive',
#         'Accept': 'application/json',
#         'trace-id': 'l0O3JMuab7dWyvdGSuV_r',
#         'platform': 'PC',
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
#         # Already added when you pass json=
#         # 'Content-Type': 'application/json',
#         'Origin': 'http://qa-a.reta-inc.com',
#         'Referer': 'http://qa-a.reta-inc.com/login',
#         'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
#         # Requests sorts cookies= alphabetically
#         # 'Cookie': 'p_h5_u=B0B5C5A2-81CF-4FE4-8323-841C0B572EDA; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2241%22%2C%22first_id%22%3A%2217e9963bdb8ae3-093e3a033b10ed-133a6253-2073600-17e9963bdb957f%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfbG9naW5faWQiOiI0MSIsIiRpZGVudGl0eV9jb29raWVfaWQiOiIxN2U5OTYzYmRiOGFlMy0wOTNlM2EwMzNiMTBlZC0xMzNhNjI1My0yMDczNjAwLTE3ZTk5NjNiZGI5NTdmIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2241%22%7D%2C%22%24device_id%22%3A%2217e9963bdb8ae3-093e3a033b10ed-133a6253-2073600-17e9963bdb957f%22%7D',
#     }

#     json_data = {
#         'email': 'conglin@reta-inc.com',
#         'password': 'woodspy',
#     }

#     response = requests.post('http://qa-a.reta-inc.com/qj/v1/auth/token/login/email', headers=headers, cookies=cookies, json=json_data, verify=False)

#     # 断言
#     assert response.status_code < 400
#     # 提取
#     print (response.json())
#     #user_id = jmespath.search("id", response.json())
# from django.test import TestCase
from playwright.sync_api import Page
from playwright.sync_api import Playwright, sync_playwright, expect
# from tep.fixture import *
import pytest
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

# def loginAdmin(page, ticket) -> None:
#     admin='obj-{"id":16,"username":"conglin","email":"conglin@reta-inc.com","mobile":"123","status":0,"roleId":1,"role":{"id":1,"name":"admin","remark":null,"createdBy":null,"createdAt":1664321323000,"modifiedBy":null,"modifiedAt":1664321323000},"customer":null}'
#     page.evaluate(f"""
#                     document.cookie = "ticket={ticket};domain=.minnov.se;path=/"
#                     localStorage.setItem('_user_','{admin}');
#                   """)

# def test_create_account(page: Page) -> None:

#     page.goto("http://dev.e.minnov.se:8888/login")
#     page.wait_for_timeout(1000)
#     # 管理员
#     ticket = "8d0d781d-1aff-4ac8-b631-190688b21fc7"
#     loginAdmin(page, ticket)
#     page.wait_for_timeout(1000)
#     page.goto("http://dev.e.minnov.se:8888/organization/account")

#     page.get_by_role("button", name="Create Account").click()

#     page.locator("input[name=\"username\"]").click()

#     page.locator("input[name=\"username\"]").fill("test")

#     page.get_by_role("dialog", name="Create Account").get_by_role("textbox", name="Please select").click()

#     page.wait_for_timeout(1000)


#     page.locator("#el-popper-container-*").get_by_role("list").get_by_text("customer").click()
#     page.wait_for_timeout(1000)


#     page.get_by_placeholder("Please select or fill in").click()

#     page.locator("li:has-text(\"Beijing FESCO Ent Service Group Co\")").click()

#     page.locator("label:has-text(\"Inactive\") span").first.click()

#     page.get_by_text("Active").nth(2).click()

#     page.locator("input[name=\"mobile\"]").click()

#     page.locator("input[name=\"mobile\"]").fill("13810264240")

#     page.locator("input[name=\"email\"]").click()

#     page.locator("input[name=\"email\"]").fill("email@fdaf.com")

#     page.locator("input[name=\"password\"]").click()

#     page.locator("input[name=\"password\"]").fill("123213123")

#     page.get_by_role("button", name="Save").click()


from playwright.sync_api import Page,expect


# 点击操作后的等待时间
sleepTime = 1000
# 表单里input控件的类型
class InputType():
    # 日期
    DATE         = 1
    # 输入后再选择
    INPUT_CHOOSE = 2
    # 输入
    INPUT        = 3
    # 下拉选择
    DOWN_CHOOSE  = 4
    # 上传文件
    UPLOAD_FILE  = 5

# # 表单里所有控件要校验的值
# newHairTableValue={
#     'country' : "China",
#     'workLocation' : "test_Work location",
#     'positionTitle':"test_Position title",
#     'montlyBaseSalary':"test_Montly base salary",
#     'probationaryPeriod':"test_Probationary period",
#     'contractType':"Permanent",
#     'jobType':"Part time",
#     'newHireContactDetails':"New hire contact details",
#     'estimateEmploymentStartDate':"2022-11-03",
#     'jobDescriptionDetail-file':"bg.jpeg",
#     'newHirePersonalDetails-file':"bg.jpeg",
#     'offerDetails-file':"bg.jpeg",
#     'otherTerms':"test_Other terms"
# }
# # 表单里所有控件的 locator
# newHairTableLocator={
#     'country' : '',
#     'workLocation' : '',
#     'positionTitle':'',
#     'montlyBaseSalary':'',
#     'probationaryPeriod':'',
#     'contractType':'',
#     'jobType':'',
#     'newHireContactDetails':'',
#     'estimateEmploymentStartDate':'',
#     'jobDescriptionDetail-file':'',
#     'newHirePersonalDetails-file':'',
#     'offerDetails-file':'',
#     'otherTerms':'',
# }

# # 表单里所有属性名与选择器条件 的关系
# newHairTableKeyWithLocator={
#     'country' : 'Country',
#     'workLocation' : 'Work location',
#     'positionTitle':'Position title',
#     'montlyBaseSalary':'Montly base salary',
#     'probationaryPeriod':'Probationary period',
#     'contractType':'Contract type',
#     'jobType':'Job type',
#     'newHireContactDetails':'New hire contact details',
#     'estimateEmploymentStartDate':'Estimate employment start date',
#     'jobDescriptionDetail-file':'.el-upload-list__item-name >> nth=0',
#     'newHirePersonalDetails-file':'.el-upload-list__item-name >> nth=1',
#     'offerDetails-file':'.el-upload-list__item-name >> nth=2',
#     'otherTerms':'.el-textarea__inner',
# }

# # 表单里所有属性名
# newHairTableKeys=('country','workLocation','positionTitle','montlyBaseSalary','probationaryPeriod','contractType','jobType','newHireContactDetails','estimateEmploymentStartDate','jobDescriptionDetail-file','newHirePersonalDetails-file','offerDetails-file','otherTerms')

# 优化思路：利用 keys 自动生成 tableValue 和 tableLocator

# # 利用要校验的值元组、属性名元组生成  两者对应关系的字典
# def generateTableValueDictByKey(tableValue,tableKeys):
#     # tableCheckValue = {}
#     # for index in range(0,len(tableKeys)):
#     #     tableCheckValue[tableKeys[index]]=tableValue[index]
#     # return tableCheckValue
#     return generateDisByTowTuple(tableKeys,tableValue)

# # 利用要选择器元组、属性名元组生成  两者对应关系的字典
# def generateTableKeyWithLocatorDictByKey(tableKeyWithLocator,tableKeys):
#     # tableKeyWithLocatorDisc = {}
#     # for index in range(0,len(tableKeys)):
#     #     tableKeyWithLocatorDisc[tableKeys[index]]=tableKeyWithLocator[index]
#     # return tableKeyWithLocatorDisc
#     return generateDisByTowTuple(tableKeys,tableKeyWithLocator)


# 通过两个元组生成第一个作为 key 第二个作为 value 的字典
def generateDisByTowTuple(tupleKey,tupleValue):
    tableKeyWithLocator = {}
    for index in range(0,len(tupleKey)):
        tableKeyWithLocator[tupleKey[index]]=tupleValue[index]
    return tableKeyWithLocator

@pytest.fixture()
def customer_data() -> None:
  class Clazz:
    ticket = '3f85a1d6-1ba8-417c-ad2b-cedd00582765'
    user = """{"id":3,"username":"customer-name","email":"customer@minnov.se","mobile":"1234566789","status":0,"roleId":2,"role":{"id":2,"name":"customer","remark":null,"createdBy":null,"createdAt":1664321323000,"modifiedBy":null,"modifiedAt":1664321323000},"customer":{"id":18,"customerFullName":"Beijing FESCO Ent Service Group Co","customerStatus":1,"contractId":"18_0928_2022","projectId":null,"taxId":null,"legalStatus":"company with limited liability","fieldOfBusiness":null,"registeredOfficeCountry":"China","registeredOfficeRegion":null,"registeredOfficeCity":null,"registeredOfficePostal":null,"registeredOfficeStreet":null,"registeredOfficeNo":null,"postAddressCountry":"China","postAddressRegion":"Beijing","postAddressCity":"Beijing","postAddressPostal":"100022","postAddressStreet":"12th floor, FESCO Mansion B","postAddressNo":null,"postAddressTelephone":null,"postAddressFax":null,"contractorFullName":null,"contractorFirstname":null,"contractorSurname":null,"contractorEmail":null,"contractorTelephone":null,"contractorPosition":null,"customerContactPersonFirstname":null,"customerContactPersonSurname":null,"customerContactPersonEmail":null,"customerContactPersonTelephone":null,"customersBankName":null,"customersBankAddress":null,"customersBankAccountName":null,"customersBankAccountNumber":null,"customersBankGiro":null,"customersBankBicSwift":null,"customersBankIban":null,"customersBankCurrency":null,"invoicingPersonFirstname":null,"invoicingConfirmationSurname":null,"invoicingConfirmationEmail":null,"invoicingConfirmationTelephone":null,"invoicingConfirmationDuoDate":null,"invoicingConfirmationCurrency":null,"invoiceReceivingFirstname":null,"invoiceReceivingSurname":null,"invoiceReceivingEmail":null,"invoiceReceivingTelephone":null,"createdBy":1,"createdAt":1664329784000,"modifiedBy":1,"modifiedAt":1666233342000,"customerServiceList":[{"id":1,"customerId":18,"serviceCatalogCode":"WP_2022-10-18","serviceRawId":4,"unit":"Per hour","qty":"10","price":"100","vat":"111","currency":"USD","serviceStatus":0,"remark":null,"createdBy":1,"createdAt":1666084008000,"modifiedBy":1,"modifiedAt":1666233342000},{"id":2,"customerId":18,"serviceCatalogCode":"PD_2022-10-18","serviceRawId":2,"unit":"Per hour","qty":"199","price":"100","vat":"111","currency":"USD","serviceStatus":0,"remark":null,"createdBy":1,"createdAt":1666084008000,"modifiedBy":1,"modifiedAt":1666233342000},{"id":3,"customerId":18,"serviceCatalogCode":"PS_2022-10-20","serviceRawId":3,"unit":"Per hour","qty":"2","price":"12","vat":"2","currency":"USD","serviceStatus":0,"remark":"1111","createdBy":1,"createdAt":1666233342000,"modifiedBy":1,"modifiedAt":1666233342000}]}}"""
  return Clazz


@pytest.fixture()
def admin_data() -> None:
    class Clazz:
        ticket = '3f85a1d6-1ba8-417c-ad2b-cedd00582765'
        user = """{"id":16,"username":"conglin","email":"conglin@reta-inc.com","mobile":"123","status":0,"roleId":1,"role":{"id":1,"name":"admin","remark":null,"createdBy":null,"createdAt":1664321323000,"modifiedBy":null,"modifiedAt":1664321323000},"customer":null}"""
    return Clazz

@pytest.fixture()
def loginCustomer(page, customer_data) -> None:
    class Clazz:
        token = customer_data.ticket

        @classmethod
        def login(cls):
            page.goto("http://qa-e.minnov.se/login")
            ticket = customer_data.ticket
            user = f'obj-{customer_data.user}'
            page.evaluate(f"""
                            document.cookie = "ticket={ticket};domain=.minnov.se;path=/"
                            localStorage.setItem('_user_','{user}');
                          """)

    return Clazz

@pytest.fixture()
def loginAdmin(page, admin_data) -> None:
    class Clazz:
        token = admin_data.ticket

        def login(self):
            page.goto("http://qa-e.minnov.se/login")
            ticket = admin_data.ticket
            user = f'obj-{admin_data.user}'
            page.evaluate(f"""
                            document.cookie = "ticket={ticket};domain=.minnov.se;path=/"
                            localStorage.setItem('_user_','{user}');
                          """)

    return Clazz

# 点击符合条件的第一个元素
def clickLocator(page,locator,**text) -> None:
    if 'text' in text:
        page.locator(locator, has_text=text['text']).first.click()

    else:
        page.locator(locator).first.click()

    page.wait_for_timeout(sleepTime)

# 返回符合条件的第一个元素
def selectLocator(page,locator,**text):
    if 'text' in text:
        return page.locator(locator, has_text=text['text']).first

    else:
        return page.locator(locator).first

# 填充符合条件的第一个元素
def fillTextLocator(page,locator,text) -> None:
    fill=page.locator(locator).first
    fill.click()
    fill.fill(text)

    page.wait_for_timeout(sleepTime)

# 获取距离像素
def getDistance(str):
    return len(str) * 10

# 表单里的 input
def clickRightInput(page,leftText,inputType,**fillText) -> None:
    distance=getDistance(leftText)

    if 'text' in fillText:
        fillTextLocator(page,f'input:right-of(label:text("{leftText}"),{distance})',fillText['text'])

        if inputType ==InputType.INPUT_CHOOSE:
            clickLocator(page,f'li:near(label:text("{leftText}"),{distance})',text=fillText['text'])

    #   elif inputType == InputType.INPUT:

    else:
        clickLocator(page,f'input:right-of(label:text("{leftText}"),{distance})')

        if inputType == InputType.DATE:
            clickLocator(page,"table td.today")

        elif inputType == InputType.DOWN_CHOOSE:
            clickLocator(page,f'li:near(label:text("{leftText}"),{distance})')

# 表单里返回符合条件的第一个元素
def selectRightInput(page,leftText):
    return selectLocator(page,f'input:right-of(label:text("{leftText}"),{getDistance(leftText)})')

# 表单里的上传文件
def uploadFile(page,leftText,filePath)-> None:
    with page.expect_file_chooser() as fc_info:
        page.click(f'div.el-upload:near(label:text("{leftText}"),50)')
    file_chooser = fc_info.value
    file_chooser.set_files(filePath)

    page.wait_for_timeout(sleepTime)

# 表单校验 locator选中的控件，值是否符合预期
# 解释： 1. 通过属性名得到对应选择器
#       2. 校验选择器是否包含要校验的文本
def expectTable(expect,tableKeys,tableLocator,tableValue)-> None:
    for key in tableKeys:
        if key.endswith("-file"):
            expect(tableLocator[key]).to_contain_text(tableValue[key])
        else:
            expect(tableLocator[key]).to_have_value(tableValue[key])

# input 包括输入、输入选择、下拉选择 是一类 isInput设为 True
# file 或 textarea 需单独选择 是一类    isInput设为 False

# 属性名、属性选择器、属性名与选择器的关系、单独选择一类的分割位置
# 作用：设置表格的选择器
# 解释：1. 利用属性名得到总长度
#      2. 不同类选择器分割的位置
#      3. 通过索引获得对应属性名，再通过属性名获得对应选择器
#      4. 通过索引获得对应属性名，再通过属性名与选择器条件对应关系得到选择器条件，进而利用函数获得对应选择器
#      5. 将获得的选择器复制给对应的选择器字典
def generateTableLocator(page,tableKeys,tableKeyWithLocator,splitIndex):
    tableLocator={}
    for index in range(0,len(tableKeys)):
        if index <= splitIndex:
            tableLocator[tableKeys[index]]=selectRightInput(page,tableKeyWithLocator[tableKeys[index]])
        else:
            tableLocator[tableKeys[index]]=selectLocator(page,tableKeyWithLocator[tableKeys[index]])
    return tableLocator


def test_test(page: Page, loginCustomer) -> None:
    # 客户
    loginCustomer.login()
    page.goto('http://qa-e.minnov.se/service/form-edit-119')
    # 表单里所有属性名
    newHairTableKeys=('country','workLocation','positionTitle','montlyBaseSalary','probationaryPeriod','contractType','jobType','newHireContactDetails','estimateEmploymentStartDate','jobDescriptionDetail-file','newHirePersonalDetails-file','offerDetails-file','otherTerms')

    TableValues=('China','test_Work location','test_Position title','test_Montly base salary','test_Probationary period','Permanent','Part time','New hire contact details','2022-11-03','bg.jpeg','bg.jpeg','bg.jpeg','test_Other terms')
    KeyWithLocator=('Country', 'Work location','Position title','Montly base salary',
              'Probationary period','Contract type','Job type','New hire contact details',
              'Estimate employment start date','.el-upload-list__item-name >> nth=0',
              '.el-upload-list__item-name >> nth=1','.el-upload-list__item-name >> nth=2',
              '.el-textarea__inner'
              )

    testTableValuesDisc = generateDisByTowTuple(newHairTableKeys,TableValues)
    testKeyWithLocatorDisc=generateDisByTowTuple(newHairTableKeys,KeyWithLocator)

    # setTableLocator(page,newHairTableKeys,newHairTableLocator,newHairTableKeyWithLocator,8)
    # expectTable(expect,newHairTableKeys,newHairTableLocator,newHairTableValue)
    tableLocator=generateTableLocator(page,newHairTableKeys,testKeyWithLocatorDisc,8)
    expectTable(expect,newHairTableKeys,tableLocator,testTableValuesDisc)

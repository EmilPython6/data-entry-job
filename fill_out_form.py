#FILL OUT FORM USING WEBSITE DATA:

#FORM SETTINGS: https://docs.google.com/forms/d/1m2FjaxEETdbukFURGMt1-4WrG4dS0VCkFkxfWSiZIHc/edit
#FORM: https://docs.google.com/forms/d/e/1FAIpQLSf84pfCFNBJaTlBe2Hoju-C_AaCLUUYR230xpHs81zrIHHwUQ/viewform?usp=header
#FORM RESPONSES SHEET: https://docs.google.com/spreadsheets/d/1X8-JPPfglvbruHE5IrZizYN3FQK1vXXXE_LSsNi1gVI/edit?resourcekey=&gid=556712208#gid=556712208
#PLAYWRIGHT DOCS: https://playwright.dev/python/docs/intro

from playwright.sync_api import sync_playwright

def fill_form(address, price, link):
    print(address)
    print(price)
    print(link)

    for number in range(0, len(address)):

        with sync_playwright() as p:

            #Choose browser:
            browser = p.chromium.launch(headless=True)

            #Open new tab:
            page = browser.new_page()

            #Open page:
            page.goto("https://docs.google.com/forms/d/e/1FAIpQLSf84pfCFNBJaTlBe2Hoju-C_AaCLUUYR230xpHs81zrIHHwUQ/viewform?usp=header")
            #print("Page title:", page.title())

            #Fill out fields:
            page.fill("input[type='text'] >> nth=0", address[number])
            page.fill("input[type='text'] >> nth=1", price[number])
            page.fill("input[type='text'] >> nth=2", link[number])
            page.wait_for_timeout(300)

            page.get_by_role('button', name='Submit').click()
            print(f"{number}: Form submitted!")
            browser.close()
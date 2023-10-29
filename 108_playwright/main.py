from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(10000)

    # https://playwright.dev/python/docs/locators
    # https://playwright.dev/python/docs/selectors

    page.wait_for_load_state("networkidle")
    # これ↓はうまくいかない。Log In 自体はすぐに表示されているので、未ロードの状態でクリックされてしまう。
    # page.wait_for_selector("text='Log In'")

    # 1. Home画面のログイン
    # page.get_by_role("button", name="Log In").click()
    # これ↓でもOK。''で囲った方が、Shop WomenとShopの両方があった様な場合に、正確にselectできる。
    page.locator("text='Log In'").click()

    # 2. Already a member?Log In
    page.get_by_test_id("signUp.switchToSignUp").click()
    # これは動かない。codegen中に、devtoolsでplaywright.$("text=Log In")をやると、見えないところのLog Inをselectしてしまっている。
    # page.locator("text=Log In").click()

    # 3. Log in with Email
    # page.get_by_test_id("siteMembersDialogLayout").get_by_test_id("buttonElement").click()
    page.locator("text=Log in with Email").click()
    page.screenshot(path="login.png")

    # 4. 入力
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("kohei.matsumoto.edu@gmail.com")
    page.get_by_test_id("emailAuth").get_by_label("Password").fill("111111")

    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()

    page.wait_for_load_state("networkidle")
    page.screenshot(path="loggedin.png")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

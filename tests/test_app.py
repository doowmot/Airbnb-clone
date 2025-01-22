from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    #p_tag = page.locator("p")
    h1_tag = page.locator("h1")

    # We assert that it has the text "This is the homepage."
    #expect(p_tag).to_have_text("This is the homepage.")
    expect(h1_tag).to_have_text("Welcome to MakersBnB")

def test_get_list_spaces(page, test_web_address, db_connection):
    #seed database
    db_connection.seed("seeds/makersbnb.sql")

    page.goto(f"http://{test_web_address}/spaces")
    #assert header is "Available Spaces"
    expect(page.locator('h1')).to_have_text('Available Spaces')
    expect(page.locator('.space-item')).to_contain_text('test_space_name')
    expect(page.locator('.space-item')).to_contain_text('test_space_description')
    expect(page.locator('.space-item')).to_contain_text('100')

#to check that the page loads up correctly
def test_get_a_new_space(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces/new")
    expect(page.locator('h1')).to_have_text('List a New Space')
    expect(page.locator('form')).to_be_visible()


def test_get_a_single_space(page, test_web_address, db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/spaces/1")
    expect(page.locator('h1')).to_have_text('test_space_name - Space Details')
    expect(page.locator('h2')).to_have_text('test_space_name')
    expect(page.get_by_test_id('description')).to_have_text('test_space_description')
    expect(page.get_by_test_id('price')).to_have_text('Price per night: £100')


def test_post_submit_a_new_space(page, test_web_address, db_connection):
    page.goto(f"http://{test_web_address}/spaces/new")

    page.fill('input[name="name"]', 'test_space_name')
    page.fill('input[name="description"]', 'test_space_description')
    page.fill('input[name="price"]', '100')

    page.click('input[type="submit"]')

    expect(page).to_have_url(f"http://{test_web_address}/spaces")
    #expect(page.locator('.space-item')).to_contain_text('test_space_name')



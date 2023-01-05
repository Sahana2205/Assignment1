
class Sahana_Data:
    username = "Admin"
    password = "admin123"
    invalid_username = "admin"
    invalid_password = "admin12"
    firstname = "Rock"
    middlename = "Paper"
    lastname = "Scissors"
    input_firstname = "sahana"

class Sahana_Selectors:
    input_username = "username"
    input_password = "password"
    login_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    input_invalid_username = "username"
    input_invalid_password = "password"
    pim_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    add_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    input_firstname = "firstName"
    input_middlename = "middleName"
    input_lastname = "lastName"
    save_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    edit_xpath = "(//button[@type='button']/i[@class='oxd-icon bi-pencil-fill'])[2]"
    firstname_edit = "firstName"
    edit_save = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button'
    delete_xpath = "(//button[@type='button']/i[@class='oxd-icon bi-trash'])[2]"
    confirm_xpath = "//p[text()='Are you Sure?']/parent::div/following-sibling::div[2]/child::button[2]"
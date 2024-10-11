*** Settings ***
Documentation     Testing website using SeleniumLibrary
Library           SeleniumLibrary

*** Variables ***
${URL}          https://www.saucedemo.com/
${BROWSER}          Chrome
${username}         standard_user
${password}         secret_sauce

*** Test Cases ***
Login until Checkout
    [Tags]    Login    Positive
    When User go to Login Page
    When User Input the correct Username
    And User Input the correct Password
    When User Click Login Button
    Then User is Logged In
    When User Click an Item
    And User Click Add to Cart
    And User Click Cart Icon
    And User Click Checkout Button
    And User Input First Name
    And User Input Last Name
    And User Input ZIP Code
    And User Click Continue Button
    And User Click Finish Button
    Then User Can See Thank You Page
    # Click Back Home
    [Teardown]    Close Browser

*** Keywords ***
User go to Login Page
    Open Browser    ${URL}    ${BROWSER}
    Title Should Be    Swag Labs

User Input the correct Username
    Input Text    id=user-name    ${username}

User Input the correct Password
    Input Text    id=password    ${password}

User Click Login Button
    Click Button    id=login-button

User is Logged In 
    Wait Until Element Is Visible   class=shopping_cart_link   100

User Click an Item
    Click Link      id=item_4_title_link

User Click Add to Cart
    Click Button    id=add-to-cart

User Click Cart Icon
    Click Link      class=shopping_cart_link

User Click Checkout Button
    Click Button    id=checkout

User Input First Name
    Input Text    id=first-name    Testing

User Input Last Name
    Input Text    id=last-name    LP

User Input ZIP Code
    Input Text    id=postal-code    123456

User Click Continue Button
    Click Button    id=continue

User Click Finish Button
    Click Button    id=finish

User Can See Thank You Page
    Element Should Contain     class=complete-header   Thank you for your order!

Click Back Home
    Click Button    id=back-to-products
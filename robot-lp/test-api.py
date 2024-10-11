*** Settings ***
Library         REST    https://reqres.in/
Documentation   Testing API using RESTinstance

*** Variables ***
${json}         {  "name": "morpheus", "job": "leader" }

*** Test Cases ***
Reqres.in Test using RESTinstance - GET
    [Tags]    GET    Positive
    When User GET Single User

Reqres.in Test using RESTinstance - POST
    [Tags]    POST    Positive
    When User POST Create User


*** Keywords ***
User GET Single User
    GET         /api/users/2
    Integer     response status     200
    Integer     $.data.id    2
    String      $.data.email   janet.weaver@reqres.in
    String      $.data.first_name   Janet
    String      $.data.last_name   Weaver

User POST Create User
    POST        /api/users      ${json}
    Integer     response status     201
    String      $.name   morpheus
    String      $.job   leader
    String      $.id
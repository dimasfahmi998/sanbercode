import baseLogin from "../../support/PageObject/loginPage.cy";
const loginData = require("../../fixtures/tricentis/login.json");

describe("Tricentis Test", () => {
  const BaseLogin = new baseLogin();

  it.only("Login", () => {
    cy.visit(BaseLogin.baseUrl);
    cy.get(BaseLogin.loginMenu).click();
    cy.get(BaseLogin.email).type(loginData.validEmail);
    cy.get(BaseLogin.password).type(loginData.validPassword);
    cy.get(BaseLogin.rememberme).click();
    cy.get(BaseLogin.loginBtn).click();
    cy.get(BaseLogin.logoutMenu).should("be.visible");
  });
});

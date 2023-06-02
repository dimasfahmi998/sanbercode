class baseLogin {
  email = "#Email";
  password = "#Password";
  rememberme = "#RememberMe";
  loginBtn = "form > .buttons > .button-1";
  logoutMenu = ".ico-logout";
  loginMenu = ".ico-login";
  baseUrl = "https://demowebshop.tricentis.com/";

  clickLoginMenu() {
    cy.klik(this.loginMenu);
  }
  inputEmail(email) {
    cy.ketik(this.email, email);
  }
  inputEmail(email) {
    cy.ketik(this.password, password);
  }
  clickLoginBtn() {
    cy.klik(this.loginBtn);
  }
  verifyLogout() {
    cy.get(this.loginMenu).should("be.visible");
  }
}
export default baseLogin;

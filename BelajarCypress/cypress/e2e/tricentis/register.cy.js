describe("Tricentis Test", () => {
  it("Register", () => {
    cy.visit("https://demowebshop.tricentis.com/");
    cy.get(".ico-register").click();
    cy.get("#FirstName").type("Dimas");
    cy.get("#LastName").type("Fahmi");
    cy.get("#Email").type("fahmi1@gmail.com");
    cy.get("#Password").type("Dimasfahmi1");
    cy.get("#ConfirmPassword").type("Dimasfahmi1");
    cy.get("#register-button").click();
    cy.get(".result").should("contain.text", "Your registration completed");
  });
});

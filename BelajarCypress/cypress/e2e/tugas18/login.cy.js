describe("Test", () => {
  it("Download Journal With Scihub", () => {
    cy.visit("https://sci-hub.se/");
    cy.get("#request").type("10.1109/CITSM50537.2020.9268854");
    cy.get("button").click();
    cy.get("#logo").should("be.visible");
  });
  it("Orange Login Valid", () => {
    cy.visit("https://opensource-demo.orangehrmlive.com/");
    cy.get(":nth-child(2) > .oxd-input-group > :nth-child(2) > .oxd-input").type("Admin");
    cy.get(":nth-child(3) > .oxd-input-group > :nth-child(2) > .oxd-input").type("admin123");
    cy.get(".oxd-button").click();
  });
  it.only("Orange Login Invalid", () => {
    cy.visit("https://opensource-demo.orangehrmlive.com/");
    cy.get(":nth-child(2) > .oxd-input-group > :nth-child(2) > .oxd-input").type("Adminnn");
    cy.get(":nth-child(3) > .oxd-input-group > :nth-child(2) > .oxd-input").type("admin123");
    cy.get(".oxd-button").click();
  });
});

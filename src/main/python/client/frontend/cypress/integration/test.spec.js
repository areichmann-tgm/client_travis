describe('My Test', function() {
   it('Visit Student Page', function() {
        cy.visit('http://localhost:8080/')
    })
  it('Table', function() {
        cy.visit('http://localhost:8080/')
        cy.contains('table1')

})

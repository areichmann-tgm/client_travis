describe('My Test', function() {
   it('Visit Student Page', function() {
        cy.visit('http://localhost:8080/')
    })
  it('Table Size', function() {
        cy.visit('http://localhost:8080/')
        cy.get('.table1').find('tr').should('have.length',0)
    })

})

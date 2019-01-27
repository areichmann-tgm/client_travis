describe('My Test', function() {
   it('Visit Student Page', function() {
        cy.visit('http://localhost:8080/')
    })
  it('Table Size', function() {
        cy.visit('http://localhost:8080/')
        cy.get('.table table-striped').find('tr').should('have.length',0)
    })

})

describe('My First Test', function() {
    it('Visit Student Page', function() {
        cy.visit('http://localhost:8080/')
    })

    it('Quering for Tableheaders', function(){
        cy.visit('http://localhost:8080/')
        cy.contains('ID')
        cy.contains('Email')
        cy.contains('Benutzername')
    })

    it('Checking if Buttons clickable', function(){
        cy.visit('http://localhost:8080/')
        cy.contains('Delete').click()
    })

})


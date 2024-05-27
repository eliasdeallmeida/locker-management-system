function show_current_year() {
    document.getElementById('current-year').textContent = new Date().getFullYear()
}

window.onload = function() {
    show_current_year()
}

function student_add() {
    window.alert('Aluno adicionado com sucesso!')
}

function student_delete() {
    return window.confirm('Tem certeza que deseja excluir esse aluno?')
}

function locker_delete() {
    return window.confirm('Tem certeza que deseja excluir esse armário? Isso apagará as portas desse armário também.')
}

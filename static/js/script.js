function cadastroButton() {
  if (['/cadastro.html', '/login.html'].includes(window.location.pathname)) {
    const buttonCadastro = document.querySelector('.button-cadastro-login')
    buttonCadastro.addEventListener('click', () => {
      if (window.location.pathname === '/cadastro.html') {
        window.location.pathname = '/login.html'
        buttonCadastro.classList.remove('cadastro-button')
        buttonCadastro.classList.add('login-button')
      } else {
        window.location.pathname = '/cadastro.html'
        buttonCadastro.classList.remove('login-button')
        buttonCadastro.classList.add('cadastro-button')
      }
    })
  }
}

cadastroButton()

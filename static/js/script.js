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

function menu() {
  const menu = document.querySelector('.header')
  menu.addEventListener('click', () => {
    const nav = document.querySelector('.nav')
    if (nav.style.display === 'flex') {
      nav.style.display = 'none'
    } else {
      nav.style.display = 'flex'
    }
  })
}

menu()
cadastroButton()

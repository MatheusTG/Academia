const loginButton = document.querySelector('#js-link-login')
const cadastroButton = document.querySelector('#js-link-cadastro')
const cadastroContainer = document.querySelector('.cadastro-container')
const loginContainer = document.querySelector('.login-container')

function loginActive() {
  loginButton.addEventListener('click', () => {
    const titulo = document.querySelector('#cadastro .titulo-principal')
    titulo.innerHTML = '<h1 class="titulo-principal titulo">Acesse sua conta<br>agora mesmo.</h1>'
    cadastroContainer.style.display = 'none'
    loginContainer.style.display = 'grid'
    console.log('asdh')
  })
}

function cadastroActive() {
  cadastroButton.addEventListener('click', () => {
    const titulo = document.querySelector('#cadastro .titulo-principal')
    titulo.innerHTML = '<h1 class="titulo-principal titulo">Cadastre-se<br>agora mesmo.</h1>'
    cadastroContainer.style.display = 'grid'
    loginContainer.style.display = 'none'
  })
}

loginActive()
cadastroActive()
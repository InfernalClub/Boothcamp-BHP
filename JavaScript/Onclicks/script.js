function toggleLogin() {
  const btn = document.getElementById('loginBtn');
  btn.textContent = (btn.textContent.trim() === 'Iniciar sesión') ? 'Cerrar sesión' : 'Iniciar sesión';
}

function hideAddDef() {
  document.getElementById('addDefBtn').style.display = 'none';
}

function likeDefinition(titulo) {
  alert('¡Te gustó la definición: ' + titulo + '!');
}

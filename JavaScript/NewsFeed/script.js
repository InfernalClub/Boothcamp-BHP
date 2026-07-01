document.querySelectorAll('.like-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const countEl = btn.previousElementSibling;
    const current = parseInt(countEl.textContent, 10);
    countEl.textContent = (current + 1) + ' like(s)';
    btn.classList.add('liked');
  });
});

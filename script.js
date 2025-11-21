// auto-hide flash messages after 4 seconds
window.addEventListener('DOMContentLoaded', () => {
const flash = document.querySelector('.flash');
if (flash) setTimeout(() => flash.style.display = 'none', 4000);
});
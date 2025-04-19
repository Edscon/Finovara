function MenuButtonListener() {
    
    const submenu = document.getElementById("div-menu-button");
    const icon = document.getElementById("svg-menu-button");
    
    if (!submenu || !icon) return;

    const iconMenu = '/static/svg/menu.svg';
    const iconClose = '/static/svg/x-mark.svg';

    icon.addEventListener("click", () => {
        const isCloseIcon = icon.src.includes(iconClose); // Si ya está en modo "cerrar", volver al "menu"

        icon.src = isCloseIcon ? iconMenu : iconClose;
        submenu.classList.toggle('hidden'); // Alternar la visibilidad
    });
}
MenuButtonListener();

function toggleSubmenu() {
    document.querySelectorAll('.toggle-submenu').forEach(button => {
        button.addEventListener('click', () => {
            const submenu = button.parentElement.querySelector('.submenu-content');
            submenu.classList.toggle('hidden');
        });
    })
}
toggleSubmenu();
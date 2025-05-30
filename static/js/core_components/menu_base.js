function isTouchDevice() {
  return 'ontouchstart' in window || navigator.maxTouchPoints > 0;
}

function MenuButtonListener() {
    
    const submenu = document.getElementById("div-menu-button");
    const icon_menu = document.getElementById("svg-menu-button");
    const icon_x_mark = document.getElementById("svg-x-mark-button");
    
    if (!submenu || !icon_menu || !icon_x_mark) return;

    const toggleMenu = () => {
        const isHidden = submenu.classList.contains('hidden');

        if (isHidden) {
            // Mostrar menú: quitar 'hidden' del submenu, ocultar icono menú y mostrar icono X
            submenu.classList.remove('hidden');
            icon_menu.classList.add('hidden');
            icon_x_mark.classList.remove('hidden');
        } else {
            // Ocultar menú: añadir 'hidden' al submenu, mostrar icono menú y ocultar icono X
            submenu.classList.add('hidden');
            icon_menu.classList.remove('hidden');
            icon_x_mark.classList.add('hidden');
        }
    };
    
    const eventType = isTouchDevice() ? 'touchstart' : 'click';

    [eventType].forEach(evt => {
        icon_menu.addEventListener(evt, e => {
            e.preventDefault();
            toggleMenu();
        });
        icon_x_mark.addEventListener(evt, e => {
            e.preventDefault();
            toggleMenu();
        });
    });

}
document.addEventListener('DOMContentLoaded', () => {
    MenuButtonListener();
});

function toggleSubmenu() {
    document.querySelectorAll('.toggle-submenu').forEach(button => {
        button.addEventListener('click', () => {
            const submenu = button.parentElement.querySelector('.submenu-content');
            submenu.classList.toggle('hidden');
        });
    })
}
toggleSubmenu();
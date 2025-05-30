
function MenuButtonListener() {
    
    const submenu = document.getElementById("div-menu-button");
    const icon_menu = document.getElementById("svg-menu-button");
    const icon_x_mark = document.getElementById("svg-x-mark-button");
    
    if (!submenu || !icon_menu || !icon_x_mark) return;

    const toggleMenu = () => {
        submenu.classList.toggle('hidden');
        icon_menu.classList.toggle('hidden');
        icon_x_mark.classList.toggle('hidden');
    };

    ['click', 'touchstart'].forEach(evt => {
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
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

    icon_menu.addEventListener("click", toggleMenu);
    icon_x_mark.addEventListener("click", toggleMenu);

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
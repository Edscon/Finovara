function MenuButtonListener() {
    const submenu = document.getElementById("div-menu-button");
    const icon_menu = document.getElementById("svg-menu-button");
    const icon_x_mark = document.getElementById("svg-x-mark-button");

    if (!submenu || !icon_menu || !icon_x_mark) return;

    const openMenu = () => {
        submenu.classList.remove("hidden");
        icon_menu.classList.add("hidden");
        icon_x_mark.classList.remove("hidden");
    };

    const closeMenu = () => {
        submenu.classList.add("hidden");
        icon_menu.classList.remove("hidden");
        icon_x_mark.classList.add("hidden");
    };

    const handleToggle = (e) => {
        e.preventDefault();
        if (submenu.classList.contains("hidden")) {
            openMenu();
        } else {
            closeMenu();
        }
    };

    // Solo usar un tipo de evento dependiendo del dispositivo
    const eventType = "ontouchstart" in window ? "touchstart" : "click";

    icon_menu.addEventListener(eventType, handleToggle, { passive: false });
    icon_x_mark.addEventListener(eventType, handleToggle, { passive: false });
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
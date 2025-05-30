function MenuButtonListener() {
    const submenu = document.getElementById("div-menu-button");
    const icon_menu = document.getElementById("svg-menu-button");
    const icon_x_mark = document.getElementById("svg-x-mark-button");

    if (!submenu || !icon_menu || !icon_x_mark) return;

    let isToggling = false;

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

        if (isToggling) return;
        isToggling = true;

        const isHidden = submenu.classList.contains("hidden");
        if (isHidden) {
            openMenu();
        } else {
            closeMenu();
        }

        // Esperar 300ms para volver a permitir toggle
        setTimeout(() => {
            isToggling = false;
        }, 200);
    };

    const eventType = "ontouchstart" in window ? "touchend" : "click";

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
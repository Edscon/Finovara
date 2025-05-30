function MenuToggleWithSingleButton() {
    const button = document.getElementById("menu-toggle-button");
    const iconSpan = document.getElementById("menu-toggle-icon");
    const submenu = document.getElementById("div-menu-button");

    if (!button || !iconSpan || !submenu) return;

    let isOpen = false;

    // Almacena los SVG en variables (puedes cargarlos desde el DOM si los tienes como plantillas ocultas)
    const svgMenu = `{% inline_svg 'svg/menu.svg' %}`;
    const svgClose = `{% inline_svg 'svg/x-mark.svg' %}`;

    button.addEventListener("click", () => {
        isOpen = !isOpen;
        submenu.classList.toggle("hidden");

        iconSpan.innerHTML = isOpen ? svgClose : svgMenu;
    });
}

MenuToggleWithSingleButton();

function toggleSubmenu() {
    document.querySelectorAll('.toggle-submenu').forEach(button => {
        button.addEventListener('click', () => {
            const submenu = button.parentElement.querySelector('.submenu-content');
            submenu.classList.toggle('hidden');
        });
    })
}
toggleSubmenu();
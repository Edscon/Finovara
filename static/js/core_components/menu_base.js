function MenuButtonListener() {
    const elem = document.getElementById("mobile-button-menu");
    const submenu = document.getElementById("div-menu-button");

    if (elem) {
        elem.addEventListener("click", function () {
            const button_menu = document.getElementById("svg-menu-button");

            if (button_menu) {
                const currentSrc = button_menu.src;
                const xMark = '/static/svg/x-mark.svg';
                const menu = '/static/svg/menu.svg';

                // Comparar solo el final del src (por si el navegador lo convierte en ruta absoluta)
                if (currentSrc.includes(xMark)) {
                    button_menu.src = menu;
                } else {
                    button_menu.src = xMark;
                }
            }
        });
    }
}

MenuButtonListener();
//TogleMenu
document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.getElementById('toggleMenuButton');
    const menu = document.getElementById('menu');
    const mainPanel = document.getElementById('MainPanel');

    const widthFull = '210px';
    const widthSmall = '100px';

    toggleButton?.addEventListener('click', function () {
        const isExpanded = menu.classList.contains(`w-[${widthFull}]`);
        const newWidth = isExpanded ? widthSmall : widthFull;
        const oldWidth = isExpanded ? widthFull : widthSmall;

        menu.classList.replace(`w-[${oldWidth}]`, `w-[${newWidth}]`);
        mainPanel?.classList.replace(`ml-[${oldWidth}]`, `ml-[${newWidth}]`);
    });
});

// Floating panel close
document.addEventListener('DOMContentLoaded', function () {
    const closeBtn = document.getElementById('x-floatPanel');
    const floatPanel = document.getElementById('floatPanel');

    closeBtn.addEventListener('click', () => {
        floatPanel.style.display = 'none';
    });
});

// Search functionality for institutions
document.addEventListener('DOMContentLoaded', function () {
    const input = document.getElementById('searchInput');
    const institutions = document.querySelectorAll('#institutionsGrid > div');

    input.addEventListener('input', function () {
        const query = input.value.toLowerCase();

        institutions.forEach(function (inst) {
            const name = inst.querySelector('span').textContent.toLowerCase();
            inst.style.display = name.includes(query) ? 'flex' : 'none';
        });
    });
});


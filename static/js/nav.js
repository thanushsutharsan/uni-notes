// controls the responsive navigation menu on tablet and mobile screens.

document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.querySelector(".nav-toggle");
    const menu = document.querySelector("#main-nav-links");

    if (!toggle || !menu) {
        return;
    }

    const closeMenu = () => {
        toggle.setAttribute("aria-expanded", "false");
        toggle.setAttribute("aria-label", "Open navigation menu");
        menu.classList.remove("is-open");
    };

    toggle.addEventListener("click", () => {
        const isOpen = toggle.getAttribute("aria-expanded") === "true";
        toggle.setAttribute("aria-expanded", String(!isOpen));
        toggle.setAttribute(
            "aria-label",
            isOpen ? "Open navigation menu" : "Close navigation menu"
        );
        menu.classList.toggle("is-open", !isOpen);
    });

    menu.addEventListener("click", (event) => {
        if (event.target.closest("a") || event.target.closest(".link-button")) {
            closeMenu();
        }
    });

    document.addEventListener("click", (event) => {
        if (!event.target.closest(".nav") && menu.classList.contains("is-open")) {
            closeMenu();
        }
    });

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
            closeMenu();
            toggle.focus();
        }
    });

    window.addEventListener("resize", () => {
        if (window.innerWidth > 860) {
            closeMenu();
        }
    });
});

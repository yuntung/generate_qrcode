const hamburger = document.querySelector(".hamburger");
    const navMenu = document.querySelector(".nav-menu");

    function toggleMenu() {
      document.getElementById('menu').classList.toggle('active');
  }

    hamburger.addEventListener("click", () => {
      hamburger.classList.toggle("active");
      navMenu.classList.toggle("active");
    });

    document.querySelectorAll(".nav-link").forEach(n => n.addEventListener("click", () => {
      hamburger.classList.remove("active");
      navMenu.classList.remove("active");
    }));
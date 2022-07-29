const toggleBtn = document.querySelector(".navbar__toggleBtn");
const menu = document.querySelector(".navbar__menu");
const screen = window.matchMedia("screen and (min-width: 1201px)");

toggleBtn.addEventListener('click', () => {
  if(menu.style.display == "none"){
    menu.style.display = "flex";
  } else{
    menu.style.display = "none"
  }
});

screen.addEventListener("change", (e) => {
  e.preventDefault();
  if (e.matches) {
    menu.style.display = "flex";
  }
})
function navToggle() {
    const nav = document.getElementById("nav")
    nav.classList.toggle("open")
}

document.getElementById("menu")
    .addEventListener("click", navToggle)

document.getElementById("x")
    .addEventListener("click", navToggle)

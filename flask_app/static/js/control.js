const darkModeToggle = document.getElementById("darkModeToggle");
darkModeToggle.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
  darkModeToggle.innerHTML = document.body.classList.contains("dark-mode")
    ? '<span class="material-symbols-outlined">light_mode</span>'
    : '<span class="material-symbols-outlined">dark_mode</span>';
});
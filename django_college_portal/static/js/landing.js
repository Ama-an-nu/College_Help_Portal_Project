
document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("loginModal");
  const closeBtn = document.querySelector(".close");

  document.querySelectorAll(".protected").forEach(link => {
    link.addEventListener("click", (e) => {
      e.preventDefault();
      modal.style.display = "flex";
    });
  });

  closeBtn.onclick = () => modal.style.display = "none";
  window.onclick = (event) => {
    if (event.target === modal) modal.style.display = "none";
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("loginModal");
  const closeBtn = document.querySelector(".close");

  if (modal) {
    document.querySelectorAll(".protected").forEach(link => {
      link.addEventListener("click", (e) => {
        e.preventDefault();
        modal.style.display = "flex";
      });
    });

    closeBtn.onclick = () => modal.style.display = "none";
    window.onclick = (event) => {
      if (event.target === modal) modal.style.display = "none";
    }
  }
});

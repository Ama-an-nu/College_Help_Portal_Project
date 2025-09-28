


document.addEventListener("DOMContentLoaded", () => {
  const profileDropdown = document.querySelector(".profile-dropdown");
  const profileBtn = document.querySelector(".profile-btn");

  if (profileBtn && profileDropdown) {
    profileBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      profileDropdown.classList.toggle("open");
    });

   
    document.addEventListener("click", (e) => {
      if (!profileDropdown.contains(e.target)) {
        profileDropdown.classList.remove("open");
      }
    });
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const logoutTrigger = document.getElementById("logoutTrigger");
  const logoutModal = document.getElementById("logoutModal");
  const cancelLogout = document.getElementById("cancelLogout");

  if (logoutTrigger && logoutModal) {
    logoutTrigger.addEventListener("click", function (e) {
      e.preventDefault(); 
      logoutModal.style.display = "block";
    });
  }

  if (cancelLogout) {
    cancelLogout.addEventListener("click", function () {
      logoutModal.style.display = "none";
    });
  }


  window.addEventListener("click", function (event) {
    if (event.target === logoutModal) {
      logoutModal.style.display = "none";
    }
  });
});

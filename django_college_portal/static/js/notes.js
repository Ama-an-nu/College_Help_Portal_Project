document.addEventListener("DOMContentLoaded", function () {
    const subjectsBySemester = {
        1: ["Mathematics I", "Physics I", "Programming Basics", "English"],
        2: ["Mathematics II", "Physics II", "Data Structures", "Electronics"],
        3: ["Discrete Math", "Computer Networks", "OOP in Java", "DBMS"],
        4: ["Operating Systems", "Software Engineering", "Theory of Computation", "AI Basics"],
        5: ["Machine Learning", "Cloud Computing", "Compiler Design", "Web Tech"],
        6: ["Deep Learning", "Cyber Security", "Big Data", "Final Year Project"]
    };

    function updateSubjects(semesterSelectId, subjectSelectId) {
        const semesterSelect = document.getElementById(semesterSelectId);
        const subjectSelect = document.getElementById(subjectSelectId);

        semesterSelect.addEventListener("change", function () {
            const semester = this.value;
            subjectSelect.innerHTML = '<option value="">-- Select Subject --</option>';

            if (subjectsBySemester[semester]) {
                subjectsBySemester[semester].forEach(subject => {
                    const option = document.createElement("option");
                    option.value = subject;
                    option.textContent = subject;
                    subjectSelect.appendChild(option);
                });
            }
        });
    }

    
    updateSubjects("upload_semester", "upload_subject");
    updateSubjects("semester", "subject");

   
    const modal = document.getElementById("uploadModal");
    const uploadBtn = document.getElementById("uploadBtn");
    const closeModal = document.getElementById("closeModal");

    uploadBtn.onclick = () => modal.style.display = "flex";
    closeModal.onclick = () => modal.style.display = "none";
    window.onclick = (event) => {
        if (event.target === modal) modal.style.display = "none";
    };
});

document.addEventListener("DOMContentLoaded", function () {
  const messagesList = document.getElementById("django-messages");

  if (messagesList) {
    const messages = messagesList.querySelectorAll("li");
    messages.forEach((msg, index) => {
      showToast(msg.textContent, index * 500); 
    });
  }
});

function showToast(message, delay = 0) {
  setTimeout(() => {
    const container = document.getElementById("toast-container");

    const toast = document.createElement("div");
    toast.classList.add("toast");
    toast.textContent = message;
    container.appendChild(toast);

  
    setTimeout(() => toast.classList.add("show"), 100);


    setTimeout(() => {
      toast.classList.remove("show");
      setTimeout(() => toast.remove(), 500);
    }, 4000);
  }, delay);
}



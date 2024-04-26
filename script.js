document.getElementById("postForm").addEventListener("submit", function(event) {
    event.preventDefault(); 
    var title = document.getElementById("title").value;
    var description = document.getElementById("description").value;
    var attachments = document.getElementById("attachments").value;

    if (title !== "" && description !== "" && attachments !== "") {
        document.getElementById("successMessage").style.display = "block";
    } else {
        alert("Please fill in all fields.");
    }
});
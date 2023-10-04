document.getElementById("add-post-button").addEventListener("click", function() {
    document.getElementById("post-modal").style.display = "block";
});

document.getElementById("cancel-post").addEventListener("click", function() {
    document.getElementById("post-modal").style.display = "none";
});

document.getElementById("close-modal").addEventListener("click", function() {
    document.getElementById("post-modal").style.display = "none";
});

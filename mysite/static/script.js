// Показать всплывающее окно при нажатии кнопки "Добавить пост"
document.getElementById("add-post-button").addEventListener("click", function() {
    document.getElementById("post-modal").style.display = "block";
});

// Закрыть всплывающее окно при нажатии кнопки "Отмена" или крестика
document.getElementById("cancel-post").addEventListener("click", function() {
    document.getElementById("post-modal").style.display = "none";
});

document.getElementById("close-modal").addEventListener("click", function() {
    document.getElementById("post-modal").style.display = "none";
});

// Добавить обработчик отправки формы, если нужно
// document.getElementById("post-modal").addEventListener("submit", function(event) {
//     event.preventDefault();
//     // Ваши действия при отправке формы
// });

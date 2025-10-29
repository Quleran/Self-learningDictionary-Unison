document.getElementById('SelectedGroup').addEventListener('click', function() {
    const wordInput = document.getElementById('wordInput').value;
    const promptInput = document.getElementById('promptInput').value;
    const selectedGroups = []; // Здесь нужно добавить логику для сбора выбранных групп

    fetch('/button_click', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ wordInput, promptInput, groups: selectedGroups })
    })
    .then(response => response.json())
    .then(data => {
        const wordList = document.getElementById('wordList');
        wordList.innerHTML = ''; // очищаем список перед добавлением новых слов
        data.words.forEach(word => {
            const li = document.createElement('li');
            li.textContent = word;
            wordList.appendChild(li);
        });
    })
    .catch(error => console.error('Ошибка:', error));
});

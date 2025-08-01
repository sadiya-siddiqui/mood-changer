// script.js
const form = document.getElementById('journalForm');
const list = document.getElementById('journalList');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const date = document.getElementById('entryDate').value;
  const text = document.getElementById('entryText').value;
  const mood = document.getElementById('moodTag').value;

  const entry = `${date} - ${mood} ${text}`;
  const li = document.createElement('li');
  li.textContent = entry;
  list.appendChild(li);

  form.reset();
});
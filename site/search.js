const search = document.querySelector('#lesson-search');
const status = document.querySelector('#result-status');
const normalize = (text) => text.toLocaleLowerCase('az')
  .normalize('NFD').replace(/\p{Mark}/gu, '').replaceAll('ə', 'e').replaceAll('ı', 'i');

const modules = Array.from(document.querySelectorAll('[data-module]'), (module) => {
  const title = normalize(module.querySelector('h3').textContent);
  return {
    module,
    lessons: Array.from(module.querySelectorAll('li'), (row) => ({
      row, text: `${title} ${normalize(row.querySelector('.t').textContent + ' ' + row.dataset.topics)}`,
    })),
  };
});

search.closest('.search').hidden = false;
search.addEventListener('input', () => {
  const terms = normalize(search.value).trim().split(/\s+/).filter(Boolean);
  let count = 0;
  for (const { module, lessons } of modules) {
    let visible = false;
    for (const { row, text } of lessons) {
      row.hidden = !terms.every((term) => text.includes(term));
      if (!row.hidden) {
        visible = true;
        count++;
      }
    }
    module.hidden = !visible;
  }
  status.hidden = !terms.length;
  status.textContent = count ? `${count} dərs tapıldı.` : 'Uyğun dərs tapılmadı.';
});

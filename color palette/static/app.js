const form = document.querySelector('#form');

form.addEventListener('submit', function (e) {
  e.preventDefault();
  getColors();
});

const getColors = () => {
  const query = form.elements.query.value;
  fetch('/palette', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams({
      query: query,
    }),
  })
    .then((response) => response.json())
    .then(createColorBoxes);
};

function createColorBoxes(data) {
  const parent = document.querySelector('.container');
  const colors = data.colors;

  parent.innerHTML = '';

  colors.forEach((color) => {
    const div = document.createElement('div');
    div.classList.add('color');
    div.style.backgroundColor = color;
    div.style.width = `calc(100%/ ${colors.length})`;

    div.addEventListener('click', function () {
      navigator.clipboard.writeText(color);
    });

    const span = document.createElement('span');
    span.innerText = color;
    div.appendChild(span);
    parent.appendChild(div);
  });
}

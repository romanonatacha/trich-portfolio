setTimeout(() => {
    const body = document.querySelector('#body_content');
    const loader = document.querySelector('#loader');

    body.classList.remove('d_none');
    loader.classList.add("d_none");
}, 1000);
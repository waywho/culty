const titleInput = document.querySelector('input[name=title]')
const slugInput = document.querySelector('input[name=slug]')

const slugify = (val) => {
	return val.toString().toLowerCase().trim()
		.replace(/&/g, '-and-') // replace & and '-and-'
		.replace(/[\s\W-]+/g, '-') // replace spaces, none word chars and dsashes with a single dash
}

titleInput.addEventListener('keyup', (e) => {
	slugInput.setAttribute('Value', slugify(titleInput.value))
})
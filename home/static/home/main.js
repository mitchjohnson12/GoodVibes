console.log("hello world")

// get all the stars
const one = document.getElementById('1-star')
const two = document.getElementById('2-star')
const three = document.getElementById('3-star')
const four = document.getElementById('4-star')
const five = document.getElementById('5-star')

const form = document.querySelector('.rate-form')


const handleStarSelect = (size) => {
	const children = form.children
	for (let i=0; i < children.length; i++) {
		if (i <= size) {
			children[i].classList.add('checked')
		} else {
			children[i].classList.remove('checked')
		}
	}
}

const handleSelect = (selection) => {
	switch(selection){
		case '1-star': {
			handleStarSelect(1)
			return
		}
		case '2-star': {
			handleStarSelect(2)
			return
		}
		case '3-star': {
			handleStarSelect(3)
			return
		}
		case '4-star': {
			handleStarSelect(4)
			return
		}
		case '5-star': {
			handleStarSelect(5)
			return
		}
	}
}


const arr = [one, two, three, four, five]

const getNumericValue = (stringValue) =>{
	let numericValue;
	if (stringValue === '1-star') {numericValue=1}
	else if (stringValue === '2-star') {numericValue=2}
	else if (stringValue === '3-star') {numericValue=3}
	else if (stringValue === '4-star') {numericValue=4}	
	else if (stringValue === '5-star') {numericValue=5}
	return numericValue
}


arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
	handleSelect(event.target.id)
}))

arr.forEach(item=> item.addEventListener('click', (event)=>{
	const val = event.target.id
	console.log(val)
	const strVal = getNumericValue(val)
	console.log(strVal)

	form.addEventListener('submit', e=>{
		e.preventDefault()
		// console.log(id)

	})
}))
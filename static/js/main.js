
try {
	const delbutton = document.getElementById("delbutton");
	const span = document.getElementById("message-span");
 	delbutton.addEventListener('click',()=>{
			span.classList.toggle("is-hidden")
		})
} 
catch (error) {}


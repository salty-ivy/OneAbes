const email = document.getElementById('email');

// console.log(email);
// console.log("hello");
email.addEventListener('change',()=>{
	// console.log(email.value);
	// alert("check");

	if(email.value.includes("@abes.ac.in")){
		email.classList.remove("is-danger");
	}
	else{
		email.classList.add("is-danger")
	}
})
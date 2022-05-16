const burger = document.getElementById("burger");
const nav_links = document.getElementById("nav_links");
const more_links = document.getElementById("more-links");
// console.log(burger);
// console.log(nav_links);


burger.addEventListener("click",()=>{
	nav_links.classList.toggle("is-active");
})

more_links.addEventListener("click",()=>{
	more_links.classList.toggle("is-active");
})

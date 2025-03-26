const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            console.log("Element in view:", entry.target); // Debugging log
            entry.target.classList.add("show");
        }
    });
}, { threshold: 0.1 }); // Trigger when 10% of the element is visible

document.querySelectorAll(".hidden").forEach((el) => {
    observer.observe(el);
    console.log("Observing:", el); // Debugging log
});
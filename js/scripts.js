let slideIndex = 0;
showSlides();

function showSlides() {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    let dots = document.getElementsByClassName("dot");
    
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}    
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";  
    dots[slideIndex-1].className += " active";
    setTimeout(showSlides, 4000); // Change image every 4 seconds
}

function currentSlide(n) {
    slideIndex = n - 1;
    showSlides();
}

function submitRating(product, rating) {
    // Replace with your data submission logic, e.g., sending to a server
    console.log(`Rating submitted for ${product}: ${rating}`);
    alert(`Thank you for rating ${product} with a score of ${rating}!`);
}
<script>
    let slideIndex = 0; // Initialize slide index
    showSlides(); // Call the function to show slides

    function showSlides() {
        let i;
        let slides = document.getElementsByClassName("mySlides"); // Get all slides
        let dots = document.getElementsByClassName("dot"); // Get all dots

        // Hide all slides
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";  
        }
        slideIndex++; // Increment slide index

        // Reset slide index if it exceeds the number of slides
        if (slideIndex > slides.length) {
            slideIndex = 1;    
        }    
        // Remove 'active' class from all dots
        for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" active", "");
        }
        // Show the current slide and mark the corresponding dot as active
        slides[slideIndex - 1].style.display = "block";  
        dots[slideIndex - 1].className += " active";

        // Change slide every 10 seconds (adjust this to your preference)
        setTimeout(showSlides, 10000); // Change image every 10 seconds
    }

    function currentSlide(n) {
        slideIndex = n; // Set slide index based on user click (changed to zero-based index)
        showSlides(); // Show the current slide
    }

    function submitRating(product, rating) {
        // Replace with your data submission logic, e.g., sending to a server
        console.log(`Rating submitted for ${product}: ${rating}`);
        alert(`Thank you for rating ${product} with a score of ${rating}!`);
    }
</script>


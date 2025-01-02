function togglePassword() {
    const passwordField = document.getElementById("password");
    const eyeIcon = document.getElementById("eye-icon");

    // Toggle the input type between 'password' and 'text'
    if (passwordField.type === "password") {
        passwordField.type = "text";  // Show password
        eyeIcon.src = "https://img.icons8.com/ios-filled/50/000000/visible.png";  // Open eye icon
    } else {
        passwordField.type = "password";  // Hide password
        eyeIcon.src = "https://img.icons8.com/ios-filled/50/000000/invisible.png";  // Closed eye icon
    }
}

function checkStrength() {
    const password = document.getElementById("password").value;
    const strengthIndicator = document.getElementById("strength-indicator");

    // Send the password to the backend for evaluation
    fetch("http://127.0.0.1:5000/check_strength", {  // Change URL to relative
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ password: password })
    })
    .then(response => response.json())
    .then(data => {
        const strength = data.strength.toLowerCase();
        strengthIndicator.textContent = data.strength;

        // Apply dynamic styling
        strengthIndicator.className = `strength ${strength.includes('weak') ? 'weak' : strength.includes('medium') ? 'medium' : 'strong'}`;
    })
    .catch(error => {
        console.error("Error:", error);
        strengthIndicator.textContent = "Error checking password strength.";
        strengthIndicator.className = "strength weak";
    });
}

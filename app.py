from flask import Flask, request, jsonify, render_template
import re
from flask_cors import CORS  # Add this import for CORS support

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def evaluate_strength(password):
    """Evaluate password strength based on enhanced criteria."""
    
    # Check for minimum length
    if len(password) < 12:
        return "Weak: Password too short, minimum length 12 characters"
    
    # Check for at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return "Weak: Include at least one uppercase letter"
    
    # Check for at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return "Weak: Include at least one lowercase letter"
    
    # Check for at least one digit
    if not re.search(r"\d", password):
        return "Weak: Include at least one number"
    
    # Check for at least one special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Medium: Add special characters for more security"
    
    # Check for no common patterns (e.g., "password", "123456")
    common_patterns = [
        "password", "123456", "12345", "1234", "123", "qwerty", "abc123", 
        "letmein", "welcome", "admin", "iloveyou", "sunshine", "monkey", 
        "qwertyuiop", "asdfghjkl", "qwerty123", "password1", "admin123", 
        "welcome123", "letmein123", "password123", "123qwe", "password1234", 
        "111111", "123321", "qwerty1234", "qwerty1", "iloveyou123", "123qwerty", 
        "dragon", "superman", "iloveu", "1q2w3e4r", "baseball", "football", 
        "michael", "welcome1234", "sunshine123", "letmein1", "monkey123", 
        "trustno1", "123abc", "qwertyui", "1qaz2wsx"
    ]
    
    if any(pattern in password.lower() for pattern in common_patterns):
        return "Weak: Avoid common patterns like 'password' or '123456'"
    
    # Check for a good mix of characters
    if len(re.findall(r"[A-Z]", password)) < 2 or len(re.findall(r"[a-z]", password)) < 2:
        return "Medium: Use more uppercase and lowercase letters"

    # Check for more than 1 number
    if len(re.findall(r"\d", password)) < 2:
        return "Medium: Include at least two numbers"

    # Check for a good mix of special characters
    if len(re.findall(r"[!@#$%^&*(),.?\":{}|<>]", password)) < 2:
        return "Medium: Add more special characters for better security"
    
    # If all checks pass, it's a strong password
    return "Strong: Your password is strong"


@app.route("/")
def home():
    # Render the index.html file from the frontend folder
    return render_template("index.html")

@app.route("/check_strength", methods=["POST"])
def check_strength():
    data = request.get_json()
    password = data.get("password", "")
    strength = evaluate_strength(password)
    return jsonify({"strength": strength})

if __name__ == "__main__":
    app.run(debug=True)

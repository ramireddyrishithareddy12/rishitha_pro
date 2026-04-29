# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data for projects (can be extended)
projects_data = [
    {
        "title": "Portfolio Website",
        "description": "Created a personal portfolio to showcase skills, projects, and achievements. Built with Flask, HTML5, CSS3, and JavaScript.",
        "technologies": ["Python", "Flask", "HTML5", "CSS3", "JavaScript"],
        "github_link": "#",
        "live_link": "#"
    },
    {
        "title": "Code Buster Challenge",
        "description": "Participated in Code Buster coding competition, demonstrating problem-solving and algorithmic thinking skills.",
        "technologies": ["C", "Data Structures"],
        "github_link": "#",
        "live_link": "#"
    }
]

@app.route('/')
def index():
    return render_template('index.html', projects=projects_data)

@app.route('/api/contact', methods=['POST'])
def contact():
    """Simple contact form endpoint"""
    data = request.get_json()
    name = data.get('name', '')
    email = data.get('email', '')
    message = data.get('message', '')
    
    # In a real application, you would send an email or save to database
    print(f"Contact Message from {name} ({email}): {message}")
    
    return jsonify({"status": "success", "message": "Thank you for reaching out! I'll get back to you soon."})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
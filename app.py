from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Official Dallas College to UT Austin CS Equivalency Map
# Source: UT Austin Transfer Guide / TCCNS
EQUIVALENCY_MAP = {
    # Computer Science Core
    "COSC 1436": "CS 312 (Intro to Programming)",
    "COSC 1437": "CS 314 (Data Structures)",
    "COSC 2436": "CS 313E (Elements of Software Design)",
    "COSC 2425": "CS 429 (Computer Organization/Architecture)",
    
    # Mathematics
    "MATH 2413": "M 408C (Calculus I)",
    "MATH 2414": "M 408D (Calculus II)",
    "MATH 2415": "M 408M (Calculus III)",
    "MATH 2318": "M 341 (Linear Algebra)",
    "MATH 2305": "CS 311D (Discrete Math)",
    
    # Science (Core Curriculum)
    "PHYS 2425": "PHY 303K/103M (Engineering Physics I)",
    "PHYS 2426": "PHY 303L/103N (Engineering Physics II)",
    
    # Core/Humanities
    "ENGL 1301": "RHE 306 (Rhetoric & Writing)",
    "ENGL 1302": "E 316L (British Literature)",
    "HIST 1301": "HIS 315L (US History to 1865)",
    "HIST 1302": "HIS 315K (US History since 1865)",
    "GOVT 2305": "GOV 310L (American Government)"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    # Standardize input to uppercase with no spaces for better matching
    user_input = data.get('course_code', '').upper().replace(" ", "")
    
    # Check for matches by removing the space in the map keys too
    match = None
    for dc_code, ut_equivalent in EQUIVALENCY_MAP.items():
        if dc_code.replace(" ", "") == user_input:
            match = ut_equivalent
            break
            
    return jsonify({
        "ut_code": match if match else "Elective / Review Needed"
    })

if __name__ == '__main__':
    app.run(debug=True)
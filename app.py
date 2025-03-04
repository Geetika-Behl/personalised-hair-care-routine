from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)


# Configure API Key (Replace with your actual key)
genai.configure(api_key="AIzaSyC2ONzC_kAGl2Er_omA3gBw6SVcqiUZ5UA")

# Load Gemini Model
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat(history=[])

# Function to get AI response
def get_llm_response(message):
    response = chat.send_message(message)
    return response.text

# Define chatbot knowledge base
haircare_info = """
You are a hair care expert AI.
Your role is to provide a personalized hair care routine and product recommendations based on hair type and scalp type.

Hair types:
1. Straight
2. Wavy
3. Curly
4. Coily

Scalp types:
1. Oily
2. Dry
3. Normal
4. Sensitive

Routine should include:
- Washing frequency
- Recommended shampoo and conditioner
- Deep conditioning treatments
- Additional hair care tips
- Suggested natural remedies

Always provide professional and helpful responses.
"""

# Flask route for homepage
@app.route('/')
def index():
    return render_template('index1.html')

# API route to generate hair care routine
@app.route('/generate_routine', methods=['POST'])
def generate_routine():
    data = request.json
    hair_type = data.get('hair_type')
    scalp_type = data.get('scalp_type')

    message = f"""
    {haircare_info}
    
    User's Hair Type: {hair_type}
    User's Scalp Type: {scalp_type}
    
    Provide a detailed hair care routine and product recommendations.
    """
    
    response = get_llm_response(message)
    return jsonify({"routine": response})

if __name__ == '__main__':
    app.run(debug=True)

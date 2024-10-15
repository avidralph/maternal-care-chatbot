from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Setup OpenAI API key (replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key)
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    user_question = request.form['question']
    response = generate_response(user_question)
    return render_template('index.html', user_question=user_question, response=response)

def generate_response(user_question):
    try:
        # Send the question to OpenAI's GPT model with a focus on maternal care
        prompt = f"Answer this question related to maternal care: {user_question}"
        
        completion = openai.Completion.create(
            engine="text-davinci-003",  # Use GPT-3 engine
            prompt=prompt,
            max_tokens=150
        )
        
        # Get the response text
        response = completion.choices[0].text.strip()
        return response
    except Exception as e:
        return "An error occurred. Please try again."

if __name__ == '__main__':
    app.run(debug=True)

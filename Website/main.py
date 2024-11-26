from flask import Flask, render_template, request, redirect, url_for, flash
import subprocess
import os

app = Flask(__name__)
app.secret_key = 'Not_So_Secret'

# Function to list programs
def list_programs():
    programs_dir = '../Test-Projects/'
    programs = []
    for folder in os.listdir(programs_dir):
        if os.path.isdir(os.path.join(programs_dir, folder)) and folder != 'website':
            programs.append(folder)
    return programs

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/programs')
def programs():
    programs = list_programs()
    return render_template('programs.html', programs=programs)

@app.route('/run_program/<program_name>')
def run_program(program_name):
    try:
        result = subprocess.run(['python', f'../Test-Projects/{program_name}/main.py'], capture_output=True, text=True, check=True)
        output = result.stdout
    except subprocess.CalledProcessError as e:
        output = f"An error occurred while running the program: {e.stderr}"
    return render_template('program_output.html', program_name=program_name, output=output)

if __name__ == '__main__':
    app.run(debug=True)
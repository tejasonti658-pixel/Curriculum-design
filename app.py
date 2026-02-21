from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse

PORT = 8000

def generate_curriculum(topic, difficulty, duration):
    return f"""
    <h2>{topic} Curriculum</h2>
    <p><b>Level:</b> {difficulty}</p>
    <p><b>Duration:</b> {duration}</p>

    <h3>Overview</h3>
    <p>This course will help you master {topic} from {difficulty} level.</p>

    <h3>Module 1</h3>
    <ul>
        <li>Introduction to {topic}</li>
        <li>Core Fundamentals</li>
        <li>Hands-on Practice</li>
    </ul>

    <h3>Final Project</h3>
    <p>Build a real-world project using {topic}.</p>
    """

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        topic = params.get("topic", [""])[0]
        difficulty = params.get("difficulty", ["Beginner"])[0]
        duration = params.get("duration", ["4 Weeks"])[0]

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if topic:
            result = generate_curriculum(topic, difficulty, duration)
        else:
            result = ""

        html = f"""
<!DOCTYPE html>
<html>
<head>
<title>GenAI Curriculum Generator</title>
<style>
    body {{
        margin: 0;
        font-family: 'Segoe UI', sans-serif;
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }}

    .container {{
        background: white;
        color: #333;
        padding: 40px;
        border-radius: 12px;
        width: 500px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.3);
    }}

    h1 {{
        text-align: center;
        margin-bottom: 30px;
        color: #2a5298;
    }}

    input, select {{
        width: 100%;
        padding: 10px;
        margin: 10px 0 20px 0;
        border-radius: 6px;
        border: 1px solid #ccc;
        font-size: 14px;
    }}

    button {{
        width: 100%;
        padding: 12px;
        background: #2a5298;
        color: white;
        border: none;
        border-radius: 6px;
        font-size: 16px;
        cursor: pointer;
        transition: 0.3s;
    }}

    button:hover {{
        background: #1e3c72;
    }}

    .result {{
        margin-top: 30px;
        padding: 20px;
        background: #f4f6f9;
        border-radius: 8px;
    }}
</style>
</head>

<body>
<div class="container">
    <h1>🎓 GenAI Curriculum Generator</h1>

    <form method="get">
        <label>Topic</label>
        <input type="text" name="topic" placeholder="Enter topic">

        <label>Difficulty</label>
        <select name="difficulty">
            <option>Beginner</option>
            <option>Intermediate</option>
            <option>Advanced</option>
        </select>

        <label>Duration</label>
        <select name="duration">
            <option>1 Week</option>
            <option>4 Weeks</option>
            <option>3 Months</option>
        </select>

        <button type="submit">Generate Curriculum</button>
    </form>

    <div class="result">
        {result}
    </div>
</div>
</body>
</html>
"""

        self.wfile.write(html.encode())

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), MyHandler)
    print(f"Server running at http://localhost:{PORT}")
    server.serve_forever()
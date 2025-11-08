from flask import Flask, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>CI/CD Demo</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 flex items-center justify-center h-screen">
    <div class="bg-white shadow-xl rounded-2xl p-10 text-center w-96">
        <h1 class="text-3xl font-bold text-indigo-600">🚀 Jenkins + Docker CI/CD</h1>
        <p class="mt-4 text-gray-600">Flask app has been successfully deployed by sahithi</p>
        <div class="mt-6">
            <span class="inline-block bg-green-100 text-green-700 px-4 py-2 rounded-full text-sm font-medium">
                Deployment Status: LIVE ✅
            </span>
        </div>
        <button onclick="location.reload()" 
                class="mt-6 px-5 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition">
            Refresh
        </button>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(TEMPLATE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

import base64

# Open the MP3 file and encode it in Base64
with open(r"C:\Users\yashu\Desktop\Zeinab\React (CWH)\serverless-music-app\Serverless\BlindingLights.mp3", "rb") as file:
    base64_encoded = base64.b64encode(file.read()).decode('utf-8')

print(base64_encoded)  # Copy this output for the API request

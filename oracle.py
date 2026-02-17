import subprocess
import requests
import sys

def run_oracle(command):
    print(f"👁️ Oracle is watching: {' '.join(command)}")
    
    try:
        # We try to run the command
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        
        if result.returncode != 0:
            analyze_error(command, result.stderr)
        else:
            print(result.stdout)
            print("\n✅ Run successful!")

    except FileNotFoundError:
        # This catches the exact error you just had!
        analyze_error(command, f"Windows cannot find the command '{command[0]}'. It is not a recognized program.")
    except Exception as e:
        analyze_error(command, str(e))

def analyze_error(command, error_text):
    print("\n❌ ERROR DETECTED. WAKING UP AI...")
    print(f"Details: {error_text}")
    
    prompt = f"The user tried to run this command on Windows: {' '.join(command)}\nIt failed with this error: {error_text}\nExplain why it failed and give the correct Windows command."

    print("\n🧠 AI is thinking (using RTX 5070)...")
    
    try:
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": "qwen2.5-coder:7b",
            "prompt": prompt,
            "stream": False,
            "keep_alive": 0
        })
        print("\n💡 ORACLE FIX:")
        print(response.json()['response'])
    except:
        print("Could not connect to Ollama. Make sure it's running!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_oracle(sys.argv[1:])
    else:
        print("Usage: python oracle.py <your_command_here>")
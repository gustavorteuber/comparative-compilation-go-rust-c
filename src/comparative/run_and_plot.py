import subprocess
import pandas as pd
import matplotlib.pyplot as plt

def run_program(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
    if result.returncode == 0:
        output = result.stdout.strip()
        if output:
            return float(output.split()[2])
    return None

def main():
    commands = {
        "Rust": "./rust_loop",
        "C++": "./cpp_loop",
        "Go": "go run go_loop.go"
    }

    times = {}
    for lang, cmd in commands.items():
        time_taken = run_program(cmd)
        if time_taken is not None:
            times[lang] = time_taken

    if not times:
        print("Erro: Nenhuma saída dos programas encontrada.")
        return

    df = pd.DataFrame(list(times.items()), columns=['Language', 'Time (seconds)'])
    
    plt.figure(figsize=(10, 6))
    plt.bar(df['Language'], df['Time (seconds)'], color=['blue', 'green', 'red'])
    plt.xlabel('Language')
    plt.ylabel('Time (seconds)')
    plt.title('Execution Time Comparison')
    plt.show()

if __name__ == "__main__":
    main()

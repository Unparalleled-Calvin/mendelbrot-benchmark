import yaml
import time
import subprocess

prelude_data = {
    "cpp": {
        "explainer": "",
        "target": "target/cpp_mandelbrot",
    },
    "python": {
        "explainer": "python3",
        "target": "target/py_mandelbrot.py",
    },
    "java": {
        "explainer": "java",
        "target": "target/java_mandelbrot.class",
    },
    "javascript": {
        "explainer": "node",
        "target": "target/js_mandelbrot.js",
    },
    "golang": {
        "explainer": "",
        "target": "target/go_mandelbrot",
    },
    "rust": {
        "explainer": "",
        "target": "target/rust_mandelbrot",
    }
}

def spawn(command):
    start_time = time.perf_counter()
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    end_time = time.perf_counter()
    proces_time = end_time - start_time
    return proces_time, stdout, stderr

def compile(languages):
    print("Compiling...")
    command = ["make", "clean"]
    for language in languages:
        target = prelude_data[language]["target"]
        command.append(target)
    make_command = " ".join(command)
    spawn(make_command)
    print("All targets successfully compiled.")

def run(languages, parameters):
    print("Start benchmarking...")
    result = {}
    for language in languages:
        print(f"Running {language} mission...", end="", flush=True)
        explainer = prelude_data[language]["explainer"]
        target = prelude_data[language]["target"]
        command = map(str, [explainer, target, parameters["xmin"], parameters["xmax"], parameters["ymin"], parameters["ymax"], parameters["width"], parameters["height"], parameters["maxiter"]])
        run_command = " ".join(command)
        runtime, _, _ = spawn(run_command)
        result[language] = runtime
        print(f"Done.")
    print("All missions done.")
    return result

with open("config.yaml", "r") as f:
    content = f.read()
config = yaml.safe_load(content)
compile(config["languages"])
result = run(config["languages"], config["parameters"])
print(result)
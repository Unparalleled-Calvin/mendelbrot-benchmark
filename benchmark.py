import yaml
import time
import subprocess

prelude_data = {
    "cpp": {
        "explainer": "",
        "target": "cpp_mandelbrot",
    },
    "python": {
        "explainer": "python3",
        "target": "py_mandelbrot.py",
    },
    "java": {
        "explainer": "java",
        "target": "mandelbrot.class",
    },
    "javascript": {
        "explainer": "node",
        "target": "js_mandelbrot.js",
    },
    "golang": {
        "explainer": "",
        "target": "go_mandelbrot",
    },
    "rust": {
        "explainer": "",
        "target": "rust_mandelbrot",
    }
}

def spawn(command, cwd=None):
    start_time = time.perf_counter()
    process = subprocess.Popen(command, cwd=cwd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    end_time = time.perf_counter()
    proces_time = end_time - start_time
    return proces_time, stdout, stderr

def compile(languages):
    print("Compiling...")
    command = ["make", "clean"]
    for language in languages:
        target = "target/" + prelude_data[language]["target"]
        command.append(target)
    make_command = " ".join(command)
    _, _, err = spawn(make_command)
    if err:
        print("Error!")
        print(err.decode())
        exit()
    else:
        print("All targets successfully compiled.")

def run(languages, parameters):
    print("Start benchmarking...")
    result = {}
    for language in languages:
        print(f"Running {language} mission...", end="", flush=True)
        explainer = prelude_data[language]["explainer"]
        if language == "java":
            target = prelude_data[language]["target"].split(".")[0]
        else:
            target = "./" + prelude_data[language]["target"]
        command = map(str, [explainer, target, parameters["xmin"], parameters["xmax"], parameters["ymin"], parameters["ymax"], parameters["width"], parameters["height"], parameters["maxiter"]])
        run_command = " ".join(command)
        runtime, _, err = spawn(run_command, cwd="target")
        if err:
            print("Error!")
            print(err.decode())
            exit()
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
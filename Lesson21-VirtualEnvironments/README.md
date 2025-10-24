````markdown
# Lesson21-VirtualEnvironments

This lesson introduces Python virtual environments (venv). It explains how to create, activate, and use virtual environments to manage project-specific dependencies, isolating them from other projects and the system Python installation.

## Key Concepts

- What virtual environments are and why they're important
- Creating virtual environments with `python -m venv`
- Activating and deactivating virtual environments
- Installing packages within virtual environments
- Managing dependencies with `requirements.txt`
- Best practices for project structure
- Checking if you're in a virtual environment

## Why Use Virtual Environments?

Virtual environments allow you to isolate dependencies for each Python project, so packages installed for one project do not affect others. This is essential for:

- **Avoiding version conflicts** between projects
- **Keeping your workspace clean** and organized
- **Ensuring reproducibility** across different machines
- **Testing different package versions** safely
- **Matching production environments** in development

## Code Explanation

The script demonstrates:
- **Example 1**: Understanding what virtual environments are
- **Example 2**: Checking the current Python environment
- **Example 3**: Viewing environment variables and paths
- **Example 4**: Listing installed packages
- **Example 5**: Using third-party libraries (requests)
- **Example 6**: Virtual environment commands reference
- **Example 7**: Recommended project structure
- **Example 8**: Best practices checklist
- **Example 9**: Complete workflow example
- **Example 10**: Common troubleshooting tips

## Expected Output

```
=== EXAMPLE 1: Understanding Virtual Environments ===

What is a virtual environment?
  • An isolated Python environment for each project
  • Separate package installations per project
  • Prevents dependency conflicts
  • Makes projects portable and reproducible

=== EXAMPLE 2: Current Python Environment ===

Python executable: /Users/jack/playground/101-python/Lesson21-VirtualEnvironments/venv/bin/python
Python version: 3.11.5
Python path: /Users/jack/playground/101-python/Lesson21-VirtualEnvironments/venv

✓ Running in a virtual environment!
  Base Python: /usr/local/opt/python@3.11
  Virtual env: /Users/jack/playground/101-python/Lesson21-VirtualEnvironments/venv

=== EXAMPLE 3: Environment Information ===

Environment variables:
  PATH: /Users/jack/playground/101-python/Lesson21-VirtualEnvironments/venv/bin:...
  VIRTUAL_ENV: /Users/jack/playground/101-python/Lesson21-VirtualEnvironments/venv

Python sys.path (where Python looks for modules):
  1. /Users/jack/playground/101-python/Lesson21-VirtualEnvironments
  2. /usr/local/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python311.zip
  3. /usr/local/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python3.11
  ... and 3 more paths

=== EXAMPLE 4: Checking Installed Packages ===

Number of installed packages: 15

Checking for common packages:
  ✓ pip             version 23.2.1
  ✓ setuptools      version 68.0.0
  ✓ requests        version 2.31.0
  ✗ numpy           not installed
  ✗ pandas          not installed

=== EXAMPLE 5: Using Requests Library ===

This example demonstrates using a third-party library.
If you see an error, install requests with:
  pip install requests

✓ requests library is installed
  Version: 2.31.0

Making a test API request...
  Status code: 200
  ✓ Successfully connected to GitHub API
  API version: https://api.github.com/user

[... Examples 6-10 show reference information ...]

============================================================
✅ Virtual Environment lesson completed!
============================================================

📚 Key Takeaways:
  • Virtual environments isolate project dependencies
  • Use 'python -m venv venv' to create one
  • Always activate before installing packages
  • Use requirements.txt to share dependencies
  • Never commit venv/ to version control

🎉 Congratulations on completing the Python 101 course!
   You now have a solid foundation in Python programming!
```

## Step-by-Step Instructions

### 1. Navigate to this lesson's directory

```sh
cd Lesson21-VirtualEnvironments
```

### 2. Create a virtual environment named `venv`

```sh
python3 -m venv venv
```

This creates a folder called `venv` containing a standalone Python installation.

### 3. Activate the virtual environment

**On macOS/Linux:**
```sh
source venv/bin/activate
```

**On Windows:**
```sh
venv\Scripts\activate
```

When activated, your shell prompt will change to show `(venv)`.

### 4. Install dependencies inside the virtual environment

```sh
pip install requests
```

This installs the `requests` package only for this project.

### 5. Run the demo script

```sh
python Lesson21-VirtualEnvironments.py
```

The script will show information about your virtual environment and make a test API request.

### 6. Deactivate the virtual environment when done

```sh
deactivate
```

This returns your shell to the global Python environment.

## Summary of Commands

| Command | Purpose |
|---------|---------|
| `python3 -m venv venv` | Create a new virtual environment |
| `source venv/bin/activate` | Activate (macOS/Linux) |
| `venv\Scripts\activate` | Activate (Windows) |
| `pip install <package>` | Install a package in the venv |
| `pip install -r requirements.txt` | Install all requirements |
| `pip freeze > requirements.txt` | Save current packages |
| `pip list` | Show installed packages |
| `deactivate` | Exit the virtual environment |

## Best Practices

1. ✅ **Always use virtual environments** for Python projects
2. ✅ **Create one venv per project** to avoid conflicts
3. ✅ **Activate before installing** packages
4. ✅ **Use requirements.txt** to track dependencies
5. ✅ **Add `venv/` to `.gitignore`** - never commit it
6. ✅ **Document setup steps** in your README
7. ✅ **Use meaningful names** for project directories
8. ✅ **Update requirements.txt** when adding packages

## Project Structure Example

```
my_project/
├── venv/                      # Virtual environment (not in git)
├── .gitignore                 # Should include venv/
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
├── src/
│   ├── __init__.py
│   └── main.py
└── tests/
    └── test_main.py
```

## `.gitignore` Example

```
# Virtual environment
venv/
env/
ENV/

# Python cache
__pycache__/
*.py[cod]
*$py.class

# IDE
.vscode/
.idea/
```

## Troubleshooting

### Virtual environment not activating?
- Make sure you're using the correct path: `source ./venv/bin/activate`
- On Windows, you might need to enable script execution:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

### Packages installing globally instead of in venv?
- Check your prompt for `(venv)` indicator
- Verify with: `which python` (should show path inside venv)

### Python version incorrect in venv?
- Create venv with specific version: `python3.11 -m venv venv`
- Check available versions: `ls /usr/bin/python*`

## Next Steps

Now that you understand virtual environments:

1. Create a venv for your own projects
2. Practice the workflow: create → activate → install → work → deactivate
3. Share your `requirements.txt` with collaborators
4. Explore tools like `virtualenvwrapper` or `pyenv` for advanced workflows
5. Learn about Docker for even more isolated environments

🎓 **Congratulations!** You've completed the Python 101 course!

````

````

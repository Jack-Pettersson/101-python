# Lesson20-Dependencies

This lesson introduces dependency management in Python. It explains how to install and import third-party modules using pip, how to specify dependencies with `requirements.txt`, and how to manage package versions for reproducible environments.

## Key Concepts

- Installing third-party packages with `pip`
- Using `requirements.txt` to specify project dependencies
- Version pinning and constraints (e.g., `>=2.25.0,<3.0.0`)
- The `pip freeze` command for generating lock files
- Importing and using external packages
- Python Package Index (PyPI)

## Code Explanation

The script demonstrates:
- How to import a third-party module (e.g., requests).
- How to use pip to install dependencies.
- How to specify dependencies and version constraints in requirements.txt.
- How to generate a lock file with `pip freeze` for reproducible installations.
- The `requests` library is used for making HTTP requests.

## Expected Output

If the `requests` library is installed:

```
=== EXAMPLE 1: Using the requests Library ===

Status code: 200
Content type: application/json; charset=utf-8
✓ Successfully connected to GitHub API

=== EXAMPLE 2: Making API Requests ===

Fetching data for user: octocat

User Information:
  Name: The Octocat
  Login: octocat
  Public Repos: 8
  Followers: 9387
  Following: 9
  Bio: N/A

=== EXAMPLE 3: Working with JSON Data ===

Found 8 repositories

First 5 repositories:
  • Hello-World
    Description: My first repository on GitHub!
    Stars: ⭐ 2043

  • Spoon-Knife
    Description: This repo is for demonstration purposes only.
    Stars: ⭐ 12345

  [... more repositories ...]

=== EXAMPLE 4: Request Parameters ===

Searching for top Python repositories...
Total results: 5,234,567

Top 3 Python repositories:

1. tensorflow/tensorflow
   ⭐ Stars: 185,234
   Description: An Open Source Machine Learning Framework for Everyone...

2. python/cpython
   ⭐ Stars: 61,890
   Description: The Python programming language...

3. django/django
   ⭐ Stars: 78,123
   Description: The Web framework for perfectionists with deadlines...

=== EXAMPLE 5: Error Handling with Requests ===

Testing: Valid URL
  ✓ Success (Status: 200)

Testing: 404 Not Found
  ⚠ Error: 404 Client Error: Not Found...

=== EXAMPLE 6: Understanding requirements.txt ===

The requirements.txt file lists all dependencies:
  requests>=2.25.0,<3.0.0

This means:
  • Install 'requests' package
  • Version must be >= 2.25.0
  • Version must be < 3.0.0

Why version constraints?
  • Ensure compatibility
  • Avoid breaking changes
  • Reproducible environments

=== EXAMPLE 7: Package Management Commands ===

Common pip commands:

📦 Install a package:
  pip install requests

📦 Install from requirements.txt:
  pip install -r requirements.txt

📦 Show installed packages:
  pip list

📦 Show package details:
  pip show requests

📦 Freeze installed packages:
  pip freeze > requirements-lock.txt

📦 Uninstall a package:
  pip uninstall requests

📦 Upgrade a package:
  pip install --upgrade requests

=== EXAMPLE 8: Checking Installation ===

Checking package availability:

✓ requests         - HTTP library for making requests
✓ json             - JSON encoder/decoder (built-in)
✓ datetime         - Date and time handling (built-in)

=== Best Practices ===

1. Always use requirements.txt for project dependencies
2. Pin versions to ensure reproducibility
3. Use virtual environments (see Lesson 21)
4. Keep dependencies up to date but test before upgrading
5. Only include packages you actually use
6. Document why each dependency is needed

✅ Dependency management lesson completed!

Next: Learn about virtual environments in Lesson 21!
```

**Note:** API data and star counts will vary based on current GitHub data.

## How to Run

1. Open a terminal and navigate to the `Lesson20-Dependencies` directory.
2. Install dependencies with:

   ```sh
   pip install -r requirements.txt
   ```

3. Run the script with:

   ```sh
      python3 Lesson20-Dependencies.py
   ```

````
   ```

Observe the output to see how third-party modules are used.

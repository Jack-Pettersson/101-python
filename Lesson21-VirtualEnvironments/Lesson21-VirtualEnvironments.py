"""
Lesson 21: Virtual Environments
Virtual environments isolate project dependencies.
This prevents conflicts between different projects.
"""

import sys
import os

print("=== EXAMPLE 1: Understanding Virtual Environments ===\n")

print("What is a virtual environment?")
print("  • An isolated Python environment for each project")
print("  • Separate package installations per project")
print("  • Prevents dependency conflicts")
print("  • Makes projects portable and reproducible")

print("\n=== EXAMPLE 2: Current Python Environment ===\n")

print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version.split()[0]}")
print(f"Python path: {sys.prefix}")

# Check if we're in a virtual environment
in_venv = hasattr(sys, 'real_prefix') or (
    hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
)

if in_venv:
    print(f"\n✓ Running in a virtual environment!")
    print(f"  Base Python: {sys.base_prefix}")
    print(f"  Virtual env: {sys.prefix}")
else:
    print(f"\n⚠ Not in a virtual environment (using system Python)")

print("\n=== EXAMPLE 3: Environment Information ===\n")

print("Environment variables:")
print(f"  PATH: {os.environ.get('PATH', 'Not set')[:80]}...")
print(f"  VIRTUAL_ENV: {os.environ.get('VIRTUAL_ENV', 'Not set')}")

print("\nPython sys.path (where Python looks for modules):")
for i, path in enumerate(sys.path[:5], 1):
    print(f"  {i}. {path}")
if len(sys.path) > 5:
    print(f"  ... and {len(sys.path) - 5} more paths")

print("\n=== EXAMPLE 4: Checking Installed Packages ===\n")

try:
    import pkg_resources
    
    installed_packages = [pkg.key for pkg in pkg_resources.working_set]
    print(f"Number of installed packages: {len(installed_packages)}")
    
    # Show some common packages
    important_packages = ['pip', 'setuptools', 'requests', 'numpy', 'pandas']
    print("\nChecking for common packages:")
    
    for package in important_packages:
        if package in installed_packages:
            try:
                version = pkg_resources.get_distribution(package).version
                print(f"  ✓ {package:15} version {version}")
            except:
                print(f"  ✓ {package:15} (version unknown)")
        else:
            print(f"  ✗ {package:15} not installed")
    
except ImportError:
    print("pkg_resources not available")

print("\n=== EXAMPLE 5: Using Requests Library ===\n")

print("This example demonstrates using a third-party library.")
print("If you see an error, install requests with:")
print("  pip install requests\n")

try:
    import requests
    
    print("✓ requests library is installed")
    print(f"  Version: {requests.__version__}")
    
    # Make a simple request
    print("\nMaking a test API request...")
    response = requests.get("https://api.github.com", timeout=5)
    print(f"  Status code: {response.status_code}")
    
    if response.status_code == 200:
        print("  ✓ Successfully connected to GitHub API")
        data = response.json()
        print(f"  API version: {data.get('current_user_url', 'N/A')}")
    
except ImportError:
    print("✗ requests library is NOT installed")
    print("\nTo install it:")
    print("  1. Activate your virtual environment (if using one)")
    print("  2. Run: pip install requests")
    print("  3. Or: pip install -r requirements.txt")
    
except Exception as e:
    print(f"⚠ Error making request: {e}")

print("\n=== EXAMPLE 6: Virtual Environment Commands ===\n")

print("Creating a virtual environment:")
print("  macOS/Linux:   python3 -m venv venv")
print("  Windows:       python -m venv venv")

print("\nActivating the virtual environment:")
print("  macOS/Linux:   source venv/bin/activate")
print("  Windows:       venv\\Scripts\\activate")

print("\nWhen activated, you'll see (venv) in your prompt:")
print("  (venv) $ ")

print("\nInstalling packages in the virtual environment:")
print("  pip install requests")
print("  pip install -r requirements.txt")

print("\nDeactivating the virtual environment:")
print("  deactivate")

print("\n=== EXAMPLE 7: Project Structure with Virtual Environment ===\n")

print("Typical project structure:")
print("  my_project/")
print("  ├── venv/                 # Virtual environment (don't commit)")
print("  ├── requirements.txt      # List of dependencies")
print("  ├── requirements-lock.txt # Exact versions (pip freeze)")
print("  ├── .gitignore            # Exclude venv/ from git")
print("  ├── README.md")
print("  └── src/")
print("      ├── __init__.py")
print("      └── main.py")

print("\n=== EXAMPLE 8: Best Practices ===\n")

print("1. ✓ Create a virtual environment for each project")
print("2. ✓ Always activate venv before installing packages")
print("3. ✓ Use requirements.txt to track dependencies")
print("4. ✓ Add venv/ to .gitignore")
print("5. ✓ Update requirements.txt when adding packages:")
print("     pip freeze > requirements.txt")
print("6. ✓ Share requirements.txt with your team")
print("7. ✗ Never commit the venv/ directory")
print("8. ✗ Don't install packages globally unless necessary")

print("\n=== EXAMPLE 9: Workflow Example ===\n")

print("Step-by-step workflow:")
print("\n1. Create a new project:")
print("   mkdir my_project && cd my_project")
print("\n2. Create virtual environment:")
print("   python3 -m venv venv")
print("\n3. Activate it:")
print("   source venv/bin/activate  # macOS/Linux")
print("\n4. Install dependencies:")
print("   pip install requests pandas numpy")
print("\n5. Save dependencies:")
print("   pip freeze > requirements.txt")
print("\n6. Work on your project...")
print("   python main.py")
print("\n7. When done:")
print("   deactivate")
print("\n8. Next time:")
print("   source venv/bin/activate")
print("   # Your packages are still there!")

print("\n=== EXAMPLE 10: Troubleshooting ===\n")

print("Common issues and solutions:")
print("\nProblem: 'pip: command not found'")
print("Solution: Use 'python -m pip' instead")
print("\nProblem: Installing packages globally by mistake")
print("Solution: Always check for (venv) in prompt before pip install")
print("\nProblem: venv not activating")
print("Solution: Use full path: source ./venv/bin/activate")
print("\nProblem: Different Python version in venv")
print("Solution: Create venv with specific version:")
print("  python3.11 -m venv venv")

print("\n" + "="*60)
print("✅ Virtual Environment lesson completed!")
print("="*60)

print("\n📚 Key Takeaways:")
print("  • Virtual environments isolate project dependencies")
print("  • Use 'python -m venv venv' to create one")
print("  • Always activate before installing packages")
print("  • Use requirements.txt to share dependencies")
print("  • Never commit venv/ to version control")

print("\n🎉 Congratulations on completing the Python 101 course!")
print("   You now have a solid foundation in Python programming!")

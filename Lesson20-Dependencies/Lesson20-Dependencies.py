"""
Lesson 20: Dependencies and Package Management
External packages extend Python's capabilities.
Use pip to install packages and requirements.txt to manage dependencies.
"""

print("=== EXAMPLE 1: Using the requests Library ===\n")

try:
    import requests
    
    # Make a simple GET request to GitHub API
    response = requests.get("https://api.github.com")
    print(f"Status code: {response.status_code}")
    print(f"Content type: {response.headers['Content-Type']}")
    
    # The response is successful if status code is 200
    if response.status_code == 200:
        print("✓ Successfully connected to GitHub API")
    
except ImportError:
    print("❌ The 'requests' library is not installed.")
    print("Install it with: pip install requests")
    print("Or: pip install -r requirements.txt")

print("\n=== EXAMPLE 2: Making API Requests ===\n")

try:
    import requests
    
    # Get information about a GitHub user
    username = "octocat"
    url = f"https://api.github.com/users/{username}"
    
    print(f"Fetching data for user: {username}")
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()  # Parse JSON response
        print(f"\nUser Information:")
        print(f"  Name: {data.get('name', 'N/A')}")
        print(f"  Login: {data.get('login')}")
        print(f"  Public Repos: {data.get('public_repos')}")
        print(f"  Followers: {data.get('followers')}")
        print(f"  Following: {data.get('following')}")
        print(f"  Bio: {data.get('bio', 'N/A')}")
    else:
        print(f"Error: Could not fetch user data (Status: {response.status_code})")
        
except ImportError:
    print("❌ The 'requests' library is not installed.")
except Exception as e:
    print(f"Error occurred: {e}")

print("\n=== EXAMPLE 3: Working with JSON Data ===\n")

try:
    import requests
    import json
    
    # Get a list of public repositories
    url = "https://api.github.com/users/octocat/repos"
    response = requests.get(url)
    
    if response.status_code == 200:
        repos = response.json()
        print(f"Found {len(repos)} repositories\n")
        
        # Display first 5 repositories
        print("First 5 repositories:")
        for repo in repos[:5]:
            print(f"  • {repo['name']}")
            print(f"    Description: {repo['description'] or 'No description'}")
            print(f"    Stars: ⭐ {repo['stargazers_count']}")
            print()
    
except ImportError:
    print("❌ The 'requests' library is not installed.")
except Exception as e:
    print(f"Error: {e}")

print("=== EXAMPLE 4: Request Parameters ===\n")

try:
    import requests
    
    # Use query parameters
    url = "https://api.github.com/search/repositories"
    params = {
        "q": "language:python",
        "sort": "stars",
        "order": "desc",
        "per_page": 3
    }
    
    print("Searching for top Python repositories...")
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Total results: {data['total_count']:,}\n")
        print("Top 3 Python repositories:")
        
        for i, repo in enumerate(data['items'], 1):
            print(f"\n{i}. {repo['full_name']}")
            print(f"   ⭐ Stars: {repo['stargazers_count']:,}")
            print(f"   Description: {repo['description'][:80]}...")
    
except ImportError:
    print("❌ The 'requests' library is not installed.")
except Exception as e:
    print(f"Error: {e}")

print("\n=== EXAMPLE 5: Error Handling with Requests ===\n")

try:
    import requests
    from requests.exceptions import RequestException, Timeout, ConnectionError
    
    # Test different error scenarios
    test_urls = [
        ("https://api.github.com", "Valid URL"),
        ("https://httpstat.us/404", "404 Not Found"),
        ("https://httpstat.us/500", "500 Server Error")
    ]
    
    for url, description in test_urls[:2]:  # Test first 2
        try:
            print(f"Testing: {description}")
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # Raises an exception for 4XX/5XX status codes
            print(f"  ✓ Success (Status: {response.status_code})")
        except Timeout:
            print(f"  ⚠ Request timed out")
        except ConnectionError:
            print(f"  ⚠ Connection error")
        except RequestException as e:
            print(f"  ⚠ Error: {e}")
        print()

except ImportError:
    print("❌ The 'requests' library is not installed.")

print("=== EXAMPLE 6: Understanding requirements.txt ===\n")

print("The requirements.txt file lists all dependencies:")
print("  requests>=2.25.0,<3.0.0")
print("\nThis means:")
print("  • Install 'requests' package")
print("  • Version must be >= 2.25.0")
print("  • Version must be < 3.0.0")
print("\nWhy version constraints?")
print("  • Ensure compatibility")
print("  • Avoid breaking changes")
print("  • Reproducible environments")

print("\n=== EXAMPLE 7: Package Management Commands ===\n")

print("Common pip commands:")
print("\n📦 Install a package:")
print("  pip install requests")
print("\n📦 Install from requirements.txt:")
print("  pip install -r requirements.txt")
print("\n📦 Show installed packages:")
print("  pip list")
print("\n📦 Show package details:")
print("  pip show requests")
print("\n📦 Freeze installed packages:")
print("  pip freeze > requirements-lock.txt")
print("\n📦 Uninstall a package:")
print("  pip uninstall requests")
print("\n📦 Upgrade a package:")
print("  pip install --upgrade requests")

print("\n=== EXAMPLE 8: Checking Installation ===\n")

packages = [
    ("requests", "HTTP library for making requests"),
    ("json", "JSON encoder/decoder (built-in)"),
    ("datetime", "Date and time handling (built-in)")
]

print("Checking package availability:\n")
for package_name, description in packages:
    try:
        __import__(package_name)
        print(f"✓ {package_name:15} - {description}")
    except ImportError:
        print(f"✗ {package_name:15} - NOT INSTALLED - {description}")

print("\n=== Best Practices ===\n")

print("1. Always use requirements.txt for project dependencies")
print("2. Pin versions to ensure reproducibility")
print("3. Use virtual environments (see Lesson 21)")
print("4. Keep dependencies up to date but test before upgrading")
print("5. Only include packages you actually use")
print("6. Document why each dependency is needed")

print("\n✅ Dependency management lesson completed!")
print("\nNext: Learn about virtual environments in Lesson 21!")

#!/usr/bin/env python3
"""
JSON API Examples
This script demonstrates working with JSON data from APIs, including
making HTTP requests, handling responses, and processing real-world data.
"""

import json
import os
import urllib.request
import urllib.error
from typing import Dict, List, Any, Optional
from datetime import datetime

class JSONAPIClient:
    """A simple client for making JSON API requests."""
    
    def __init__(self, base_url: str = ""):
        self.base_url = base_url
        self.headers = {
            'User-Agent': 'Python JSON API Client/1.0',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    
    def make_request(self, endpoint: str, method: str = 'GET', data: Optional[Dict] = None) -> Optional[Dict[str, Any]]:
        """Make an HTTP request and return parsed JSON response."""
        url = f"{self.base_url}{endpoint}" if self.base_url else endpoint
        
        try:
            # Prepare request
            if data and method in ['POST', 'PUT', 'PATCH']:
                json_data = json.dumps(data).encode('utf-8')
                req = urllib.request.Request(url, data=json_data, headers=self.headers, method=method)
            else:
                req = urllib.request.Request(url, headers=self.headers, method=method)
            
            # Make request
            with urllib.request.urlopen(req, timeout=10) as response:
                response_data = response.read().decode('utf-8')
                return json.loads(response_data)
                
        except urllib.error.HTTPError as e:
            print(f"❌ HTTP Error {e.code}: {e.reason}")
            if hasattr(e, 'read'):
                error_body = e.read().decode('utf-8')
                try:
                    error_json = json.loads(error_body)
                    print(f"   Error details: {error_json}")
                except:
                    print(f"   Error body: {error_body}")
            return None
            
        except urllib.error.URLError as e:
            print(f"❌ URL Error: {e.reason}")
            return None
            
        except json.JSONDecodeError as e:
            print(f"❌ JSON Decode Error: {e}")
            return None
            
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return None

def simulate_api_responses():
    """Simulate various API response scenarios using local JSON files."""
    print("=== Simulating API Responses ===\n")
    
    # Simulate different API endpoints
    api_responses = {
        '/api/users': 'sample_data.json',
        '/api/products': 'products.json',
        '/api/weather': 'weather_data.json',
        '/api/items': 'api_response.json'
    }
    
    client = JSONAPIClient()
    
    for endpoint, filename in api_responses.items():
        print(f"📡 GET {endpoint}")
        
        # Simulate API call by loading local file
        try:
            with open(filename, 'r') as file:
                response_data = json.load(file)
            
            print(f"   Status: 200 OK")
            print(f"   Content-Type: application/json")
            print(f"   Data keys: {list(response_data.keys())}")
            
            # Simulate processing based on endpoint
            if 'users' in response_data:
                print(f"   Found {len(response_data['users'])} users")
            elif 'products' in response_data:
                print(f"   Found {len(response_data['products'])} products")
            elif 'current_weather' in response_data:
                temp = response_data['current_weather']['temperature']
                print(f"   Current temperature: {temp}°C")
            elif 'data' in response_data:
                items = response_data['data'].get('items', [])
                print(f"   Found {len(items)} items")
            
            print()
            
        except FileNotFoundError:
            print(f"   ❌ File not found: {filename}")
        except Exception as e:
            print(f"   ❌ Error: {e}")

def process_weather_api():
    """Process weather API data with error handling."""
    print("=== Weather API Processing ===\n")
    
    try:
        with open('weather_data.json', 'r') as file:
            weather_data = json.load(file)
        
        # Extract and validate data
        location = weather_data.get('location', {})
        current = weather_data.get('current_weather', {})
        forecast = weather_data.get('forecast', [])
        
        print(f"🌤️  Weather for {location.get('city', 'Unknown')}, {location.get('country', 'Unknown')}")
        print(f"   Coordinates: {location.get('coordinates', {}).get('latitude', 'N/A')}, {location.get('coordinates', {}).get('longitude', 'N/A')}")
        print()
        
        # Current weather
        if current:
            print("Current Conditions:")
            print(f"   Temperature: {current.get('temperature', 'N/A')}°{current.get('unit', 'C').upper()}")
            print(f"   Humidity: {current.get('humidity', 'N/A')}%")
            print(f"   Pressure: {current.get('pressure', 'N/A')} hPa")
            print(f"   Description: {current.get('description', 'N/A')}")
            
            wind = current.get('wind', {})
            if wind:
                print(f"   Wind: {wind.get('speed', 'N/A')} {wind.get('unit', 'km/h')} {wind.get('direction', 'N/A')}")
            print()
        
        # Forecast
        if forecast:
            print("Forecast:")
            for day in forecast[:3]:  # Show next 3 days
                date = day.get('date', 'Unknown')
                high = day.get('high', 'N/A')
                low = day.get('low', 'N/A')
                desc = day.get('description', 'Unknown')
                rain_chance = day.get('precipitation_chance', 0)
                
                print(f"   {date}: {desc} (High: {high}°, Low: {low}°, Rain: {rain_chance}%)")
        
    except Exception as e:
        print(f"❌ Error processing weather data: {e}")

def process_products_api():
    """Process products API data with filtering and analysis."""
    print("\n=== Products API Processing ===\n")
    
    try:
        with open('products.json', 'r') as file:
            products_data = json.load(file)
        
        products = products_data.get('products', [])
        summary = products_data.get('inventory_summary', {})
        
        print(f"📦 Products Inventory Summary:")
        print(f"   Total products: {summary.get('total_products', 0)}")
        print(f"   In stock: {summary.get('in_stock_count', 0)}")
        print(f"   Out of stock: {summary.get('out_of_stock_count', 0)}")
        print(f"   Total value: ${summary.get('total_value', 0):.2f}")
        print()
        
        # Filter and analyze products
        in_stock_products = [p for p in products if p.get('in_stock', False)]
        expensive_products = [p for p in products if p.get('price', 0) > 50]
        
        print(f"📊 Analysis:")
        print(f"   In-stock products: {len(in_stock_products)}")
        print(f"   Expensive products (>$50): {len(expensive_products)}")
        
        # Category breakdown
        categories = {}
        for product in products:
            category = product.get('category', 'Unknown')
            categories[category] = categories.get(category, 0) + 1
        
        print(f"   Categories: {dict(categories)}")
        print()
        
        # Show product details
        print("🛍️  Product Details:")
        for product in products:
            name = product.get('name', 'Unknown')
            price = product.get('price', 0)
            category = product.get('category', 'Unknown')
            in_stock = "✅" if product.get('in_stock', False) else "❌"
            
            print(f"   {in_stock} {name} - ${price:.2f} ({category})")
        
    except Exception as e:
        print(f"❌ Error processing products data: {e}")

def create_api_response():
    """Create a realistic API response structure."""
    print("\n=== Creating API Response ===\n")
    
    # Simulate a user search API response
    api_response = {
        "status": "success",
        "code": 200,
        "message": "Users retrieved successfully",
        "data": {
            "users": [
                {
                    "id": 1,
                    "username": "johndoe",
                    "email": "john@example.com",
                    "profile": {
                        "first_name": "John",
                        "last_name": "Doe",
                        "avatar": "https://api.example.com/avatars/1.jpg",
                        "bio": "Software developer passionate about Python"
                    },
                    "stats": {
                        "posts": 42,
                        "followers": 150,
                        "following": 75
                    },
                    "created_at": "2023-01-15T10:30:00Z",
                    "last_login": "2024-01-15T14:22:00Z",
                    "is_verified": True
                },
                {
                    "id": 2,
                    "username": "janesmith",
                    "email": "jane@example.com",
                    "profile": {
                        "first_name": "Jane",
                        "last_name": "Smith",
                        "avatar": "https://api.example.com/avatars/2.jpg",
                        "bio": "Data scientist and machine learning enthusiast"
                    },
                    "stats": {
                        "posts": 28,
                        "followers": 89,
                        "following": 120
                    },
                    "created_at": "2023-03-20T16:45:00Z",
                    "last_login": "2024-01-14T09:15:00Z",
                    "is_verified": False
                }
            ],
            "pagination": {
                "page": 1,
                "per_page": 10,
                "total_pages": 1,
                "total_items": 2
            },
            "filters": {
                "search_term": "john",
                "verified_only": False,
                "sort_by": "created_at",
                "sort_order": "desc"
            }
        },
        "meta": {
            "request_id": "req_123456789",
            "timestamp": datetime.now().isoformat() + "Z",
            "version": "v1.2.0",
            "rate_limit": {
                "remaining": 999,
                "reset_time": "2024-01-16T00:00:00Z"
            }
        }
    }
    
    # Save the API response
    with open('user_search_response.json', 'w') as file:
        json.dump(api_response, file, indent=2)
    
    print("✅ Created realistic API response: user_search_response.json")
    print(f"   Status: {api_response['status']}")
    print(f"   Users found: {len(api_response['data']['users'])}")
    print(f"   Request ID: {api_response['meta']['request_id']}")

def analyze_api_response():
    """Analyze the created API response."""
    print("\n=== Analyzing API Response ===\n")
    
    try:
        with open('user_search_response.json', 'r') as file:
            response = json.load(file)
        
        # Basic response info
        print(f"📡 API Response Analysis:")
        print(f"   Status: {response.get('status')}")
        print(f"   Code: {response.get('code')}")
        print(f"   Message: {response.get('message')}")
        print()
        
        # Data analysis
        data = response.get('data', {})
        users = data.get('users', [])
        pagination = data.get('pagination', {})
        filters = data.get('filters', {})
        
        print(f"👥 User Data:")
        print(f"   Users found: {len(users)}")
        print(f"   Page: {pagination.get('page')} of {pagination.get('total_pages')}")
        print(f"   Items per page: {pagination.get('per_page')}")
        print()
        
        print(f"🔍 Search Filters:")
        for key, value in filters.items():
            print(f"   {key}: {value}")
        print()
        
        # User analysis
        verified_users = [u for u in users if u.get('is_verified', False)]
        total_posts = sum(u.get('stats', {}).get('posts', 0) for u in users)
        total_followers = sum(u.get('stats', {}).get('followers', 0) for u in users)
        
        print(f"📊 User Statistics:")
        print(f"   Verified users: {len(verified_users)}")
        print(f"   Total posts: {total_posts}")
        print(f"   Total followers: {total_followers}")
        print(f"   Average posts per user: {total_posts / len(users) if users else 0:.1f}")
        print()
        
        # Show user details
        print(f"👤 User Details:")
        for user in users:
            profile = user.get('profile', {})
            stats = user.get('stats', {})
            verified = "✅" if user.get('is_verified') else "❌"
            
            print(f"   {verified} {profile.get('first_name')} {profile.get('last_name')} (@{user.get('username')})")
            print(f"      Posts: {stats.get('posts')}, Followers: {stats.get('followers')}, Following: {stats.get('following')}")
            print(f"      Bio: {profile.get('bio', 'No bio')}")
            print()
        
        # Rate limiting info
        meta = response.get('meta', {})
        rate_limit = meta.get('rate_limit', {})
        print(f"⏱️  Rate Limiting:")
        print(f"   Remaining requests: {rate_limit.get('remaining')}")
        print(f"   Reset time: {rate_limit.get('reset_time')}")
        
    except Exception as e:
        print(f"❌ Error analyzing API response: {e}")

def main():
    """Main function to run all API examples."""
    print("JSON API Examples")
    print("=" * 50)
    
    # Change to the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Run examples
    simulate_api_responses()
    process_weather_api()
    process_products_api()
    create_api_response()
    analyze_api_response()
    
    print("\n" + "=" * 50)
    print("All API examples completed!")

if __name__ == "__main__":
    main()



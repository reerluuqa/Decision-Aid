#!/usr/bin/env python3
"""
Medical Reference Library Setup Script for GitHub Pages
Creates folder structure and index files for fast clinical reference
"""

import os
import sys

# Define all medical categories from your images
CATEGORIES = [
    "Neurology",
    "Cancer",
    "Eyes-ophthalmology",
    "Infectious-disease",
    "Paeds",
    "Mental-health",
    "Cardio-respiratory",
    "General",
    "Women's-Health",
    "Men's-Health",
    "Endocrine-metabolic",
    "GI-Gastroenterology-hepatology",
    "Skin-and-Nail",
    "ENT-and-Oral-health",
    "MSK-and-Rheumatology",
    "Pregnancy",
    "Renal-Urology",
    "Haematology",
    "Allergy",
    "Palliative",
    "Geriatrics"
]

def create_folder_structure():
    """Create all category folders"""
    print("Creating folder structure...")
    for category in CATEGORIES:
        folder_name = category.replace(" ", "-").replace("&", "and")
        os.makedirs(folder_name, exist_ok=True)
        print(f"✓ Created: {folder_name}/")
    print()

def create_category_index(category):
    """Create index.html for each category"""
    folder_name = category.replace(" ", "-").replace("&", "and")
    display_name = category.replace("-", " ").replace("and", "&")
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{display_name} - Medical Reference</title>
<style>
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    max-width: 900px;
    margin: 2rem auto;
    padding: 0 1rem;
    line-height: 1.6;
  }}
  h1 {{
    color: #2c3e50;
    border-bottom: 3px solid #3498db;
    padding-bottom: 0.5rem;
  }}
  .back-link {{
    display: inline-block;
    margin-bottom: 1rem;
    color: #3498db;
    text-decoration: none;
    font-weight: 500;
  }}
  .back-link:hover {{
    text-decoration: underline;
  }}
  ul {{
    list-style: none;
    padding: 0;
  }}
  li {{
    margin: 0.8rem 0;
    padding: 0.8rem;
    background: #f8f9fa;
    border-left: 4px solid #3498db;
    border-radius: 4px;
  }}
  li:hover {{
    background: #e9ecef;
  }}
  a {{
    color: #2c3e50;
    text-decoration: none;
    font-size: 1.1rem;
  }}
  a:hover {{
    color: #3498db;
  }}
  .empty-state {{
    text-align: center;
    padding: 3rem;
    color: #6c757d;
    font-style: italic;
  }}
</style>
</head>
<body>
<a href="../index.html" class="back-link">← Back to Main Library</a>
<h1>{display_name}</h1>
<div id="content">
  <p class="empty-state">No topics added yet. Add your HTML files to this folder and they will appear here automatically.</p>
</div>

<script>
// Auto-populate links from files in this directory
// This runs client-side, no API needed!
async function loadTopics() {{
  // For now, manually list files here as GitHub Pages doesn't allow directory listing
  // You'll update this array when you add new files
  const topics = [
    // Add your files here like: {{ file: "topic-name.html", title: "Topic Name" }}
  ];
  
  const contentDiv = document.getElementById('content');
  
  if (topics.length === 0) {{
    contentDiv.innerHTML = '<p class="empty-state">No topics added yet. Add your HTML files to this folder.</p>';
    return;
  }}
  
  let html = '<ul>';
  topics.forEach(topic => {{
    html += `<li><a href="${{topic.file}}">${{topic.title}}</a></li>`;
  }});
  html += '</ul>';
  
  contentDiv.innerHTML = html;
}}

loadTopics();
</script>
</body>
</html>'''
    
    file_path = os.path.join(folder_name, "index.html")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return folder_name

def create_main_index():
    """Create main index.html"""
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Medical Reference Library</title>
<style>
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    max-width: 1000px;
    margin: 0 auto;
    padding: 2rem 1rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
  }
  .container {
    background: white;
    border-radius: 12px;
    padding: 2rem;
    box-shadow: 0 10px 40px rgba(0,0,0,0.2);
  }
  h1 {
    color: #2c3e50;
    margin-bottom: 0.5rem;
    font-size: 2.5rem;
  }
  .subtitle {
    color: #6c757d;
    margin-bottom: 2rem;
    font-size: 1.1rem;
  }
  .search-box {
    width: 100%;
    padding: 1rem;
    font-size: 1rem;
    border: 2px solid #e9ecef;
    border-radius: 8px;
    margin-bottom: 2rem;
    box-sizing: border-box;
  }
  .search-box:focus {
    outline: none;
    border-color: #3498db;
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1rem;
    margin-top: 1.5rem;
  }
  .category-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 1.5rem;
    border-radius: 8px;
    text-decoration: none;
    color: white;
    transition: transform 0.2s, box-shadow 0.2s;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }
  .category-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.15);
  }
  .category-card h2 {
    margin: 0;
    font-size: 1.3rem;
    font-weight: 600;
  }
  .hidden {
    display: none;
  }
  @media (max-width: 768px) {
    .grid {
      grid-template-columns: 1fr;
    }
    h1 {
      font-size: 2rem;
    }
  }
</style>
</head>
<body>
<div class="container">
  <h1>🏥 Medical Reference Library</h1>
  <p class="subtitle">Fast clinical reference for busy practice</p>
  
  <input type="text" class="search-box" id="searchBox" placeholder="Search categories..." />
  
  <div class="grid" id="categoryGrid">'''
    
    for category in CATEGORIES:
        folder_name = category.replace(" ", "-").replace("&", "and")
        display_name = category.replace("-", " ").replace("and", "&")
        html_content += f'''
    <a href="{folder_name}/index.html" class="category-card" data-category="{display_name.lower()}">
      <h2>{display_name}</h2>
    </a>'''
    
    html_content += '''
  </div>
</div>

<script>
// Quick search functionality
const searchBox = document.getElementById('searchBox');
const categoryCards = document.querySelectorAll('.category-card');

searchBox.addEventListener('input', (e) => {
  const searchTerm = e.target.value.toLowerCase();
  
  categoryCards.forEach(card => {
    const categoryName = card.getAttribute('data-category');
    if (categoryName.includes(searchTerm)) {
      card.classList.remove('hidden');
    } else {
      card.classList.add('hidden');
    }
  });
});
</script>
</body>
</html>'''
    
    with open("index.html", 'w', encoding='utf-8') as f:
        f.write(html_content)

def create_readme():
    """Create README with instructions"""
    readme_content = '''# Medical Reference Library

A fast, searchable medical reference library for clinical practice.

## 🚀 Quick Start

1. **Add your HTML files** to the appropriate category folder
2. **Update the category's index.html** to list your new files
3. **Commit and push** to GitHub
4. Your site updates automatically at: `https://yourusername.github.io/Decision-Aid/`

## 📁 Folder Structure

Each medical category has its own folder with an index.html file.

## ✨ Adding New Topics

1. Create your HTML file (e.g., `diabetes-management.html`)
2. Save it in the appropriate category folder
3. Edit that category's `index.html`
4. Find the `topics` array in the JavaScript
5. Add your file:
   ```javascript
   const topics = [
     { file: "diabetes-management.html", title: "Diabetes Management" },
     // Add more here...
   ];
   ```

## 🎯 Features

- ✅ **No API limits** - Pure static HTML
- ✅ **Lightning fast** - No server calls
- ✅ **Works offline** - After first load
- ✅ **Mobile friendly** - Responsive design
- ✅ **Searchable** - Quick category filtering

## 📝 Tips

- Use clear, descriptive filenames with hyphens (not spaces)
- Keep HTML files under 1MB for fast loading
- Test locally before pushing to GitHub
- Use lowercase for all filenames

## 🔧 Maintenance

No maintenance needed! Just add files and update the index arrays.

---
Built for busy clinicians who need fast, reliable access to medical information.
'''
    
    with open("README.md", 'w', encoding='utf-8') as f:
        f.write(readme_content)

def main():
    """Main setup function"""
    print("=" * 60)
    print("Medical Reference Library Setup Script")
    print("=" * 60)
    print()
    
    # Check if we're in the right place
    if os.path.exists("index.html"):
        response = input("index.html already exists. Overwrite? (y/n): ")
        if response.lower() != 'y':
            print("Setup cancelled.")
            return
    
    print("Setting up your medical reference library...\n")
    
    # Create folders
    create_folder_structure()
    
    # Create index files
    print("Creating index files...")
    for category in CATEGORIES:
        folder_name = create_category_index(category)
        print(f"✓ Created: {folder_name}/index.html")
    print()
    
    # Create main index
    print("Creating main index.html...")
    create_main_index()
    print("✓ Created: index.html")
    print()
    
    # Create README
    print("Creating README.md...")
    create_readme()
    print("✓ Created: README.md")
    print()
    
    print("=" * 60)
    print("✅ Setup complete!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Add your HTML files to the category folders")
    print("2. Update each category's index.html to list your files")
    print("3. Commit and push to GitHub:")
    print("   git add .")
    print("   git commit -m 'Set up medical reference library'")
    print("   git push")
    print()
    print("Your site will be live at:")
    print("https://yourusername.github.io/your-repo-name/")
    print()

if __name__ == "__main__":
    main()
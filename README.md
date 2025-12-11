# Decision-Aid
30 second medical decision aid

## Quick Start

1. Add your HTML files to the appropriate category folder.
2. Update that folder's `index.html` to list your files.
3. Commit and push to GitHub; your site updates at `https://yourusername.github.io/Decision-Aid/`.

## Folder Structure

Each medical category has its own folder with an `index.html` file.

## Adding New Topics

1. Create your HTML file (e.g., `diabetes-management.html`).
2. Save it in the appropriate category folder.
3. Edit that category's `index.html`.
4. Update the `topics` array in the JavaScript:
   ```javascript
   const topics = [
     { file: "diabetes-management.html", title: "Diabetes Management" },
     // Add more here...
   ];
   ```

## Features

- No API limits; pure static HTML.
- Lightning fast; no server calls.
- Works offline after first load.
- Mobile friendly and responsive.
- Searchable with quick category filtering.

## Tips

- Use clear, descriptive filenames with hyphens (not spaces).
- Keep HTML files under 1MB for fast loading.
- Test locally before pushing to GitHub.
- Use lowercase for all filenames.

## Maintenance

Just add files and update the index arrays as needed.

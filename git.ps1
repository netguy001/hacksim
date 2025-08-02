# Create README
echo "# hacksim" > README.md

# Initialize Git repo
git init

# Add README
git add .

# Commit changes
git commit -m "first commit"

# Set main branch
git branch -M main

# Add remote origin (change this if needed)
git remote add origin https://github.com/netguy001/hacksim.git

# Push to GitHub
git push -u origin main

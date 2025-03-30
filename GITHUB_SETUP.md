# GitHub Setup Guide

This guide walks through the complete process of setting up a project on GitHub, from initial configuration to deployment.

## 1. Initial Git Setup

```bash
# Configure git with your email and name
git config --global user.email "your.email@example.com"
git config --global user.name "Your Name"

# Initialize git repository
git init

# Create .gitignore file (if not exists)
touch .gitignore
```

## 2. SSH Key Setup

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"
# Press Enter to accept default file location
# Press Enter twice for no passphrase (or enter one if preferred)

# Start the SSH agent
eval "$(ssh-agent -s)"

# Add SSH key to agent
ssh-add ~/.ssh/id_ed25519

# Copy public key to clipboard (Mac)
pbcopy < ~/.ssh/id_ed25519.pub
```

### Add SSH Key to GitHub
1. Go to GitHub.com → Settings
2. Click "SSH and GPG keys" in sidebar
3. Click "New SSH key"
4. Give it a title (e.g., "Mac")
5. Paste the key from clipboard
6. Click "Add SSH key"

## 3. Create GitHub Repository

1. Go to GitHub.com
2. Click "+" in top-right → "New repository"
3. Fill in repository details:
   - Name: `your-repo-name`
   - Description (optional)
   - Choose Public/Private
   - Don't initialize with README if you have existing code

## 4. Connect and Push to GitHub

```bash
# Add remote repository (using SSH)
git remote add origin git@github.com:username/repository.git

# Test SSH connection
ssh -T git@github.com
# Type 'yes' when prompted about host authenticity

# Stage all files
git add .

# Create initial commit
git commit -m "Initial commit"

# Push to GitHub
git push -u origin main
```

## 5. Common Git Commands

```bash
# Check repository status
git status

# View remote repositories
git remote -v

# Create new branch
git checkout -b branch-name

# Switch branches
git checkout branch-name

# Pull latest changes
git pull

# Stage changes
git add filename
# or stage all changes:
git add .

# Commit changes
git commit -m "Your commit message"

# Push changes
git push
# or for new branch:
git push -u origin branch-name
```

## 6. Best Practices

### Commit Messages
- Use clear, descriptive commit messages
- Start with a verb (e.g., "Add", "Fix", "Update")
- Keep first line under 50 characters
- Use the body for detailed explanations

### Branching
- Keep `main` branch stable
- Create feature branches for new work
- Use descriptive branch names (e.g., `feature/user-authentication`)
- Delete branches after merging

### .gitignore
Common entries to include:
```gitignore
# Environment files
.env
.venv
env/
venv/

# Python
__pycache__/
*.py[cod]
*.so

# IDE
.idea/
.vscode/
*.swp

# OS
.DS_Store
Thumbs.db
```

## 7. Troubleshooting

### Authentication Issues
```bash
# Check SSH key is added to agent
ssh-add -l

# Verify GitHub connection
ssh -T git@github.com

# Reset SSH connection
ssh-add -D
ssh-add ~/.ssh/id_ed25519
```

### Remote Issues
```bash
# Remove remote
git remote remove origin

# Add new remote
git remote add origin git@github.com:username/repository.git

# Verify remote
git remote -v
```

## 8. GitHub Features

### Issues
- Use for tracking bugs and features
- Add labels for categorization
- Reference issues in commits (#issue-number)

### Pull Requests
1. Create new branch
2. Make changes
3. Push branch
4. Create Pull Request on GitHub
5. Request reviews
6. Merge after approval

### GitHub Actions
- Automated workflows
- CI/CD pipelines
- Automated testing
- Located in `.github/workflows/`

## 9. Security Best Practices

1. Never commit sensitive data
2. Use environment variables
3. Keep dependencies updated
4. Use SSH keys instead of passwords
5. Enable two-factor authentication

## 10. Additional Resources

- [GitHub Docs](https://docs.github.com)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Skills](https://skills.github.com)
- [GitHub Guides](https://guides.github.com)

# Claude Code Skills

This directory contains custom skills for Claude Code to automate common tasks.

## Available Skills

### commit_changes.md
Automates the complete git workflow: analyze changes, generate commit message, commit locally, and push to remote repository.

## Usage

Simply ask Claude to:
- "Commit changes"
- "提交代码"
- "Push to remote"

Claude will automatically:
1. Analyze what changed
2. Generate a proper commit message
3. Commit the changes
4. Push to remote repository (GitHub/GitLab/etc.)

## Adding New Skills

To add a new skill, create a new `.md` file in this directory following the format:
- Frontmatter with description
- Detailed documentation
- Usage examples

See `commit_changes.md` for a reference implementation.

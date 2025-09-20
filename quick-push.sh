#!/bin/bash

# Quick git push script
# Usage: ./quick-push.sh "Your commit message"

MESSAGE=${1:-"Quick fix"}
git add .
git commit -m "$MESSAGE"
git push

echo "✅ Pushed: $MESSAGE"

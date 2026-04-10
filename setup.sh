#!/bin/bash

# Создаем директорию для GitHub Actions
mkdir -p .github/workflows

# Создаем файл конфигурации GitHub Actions для деплоя на GitHub Pages
cat << 'EOF' > .github/workflows/deploy-pages.yml
name: Deploy to GitHub Pages

on:
  push:
    branches: ["main", "master"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Prepare site directory
        run: |
          mkdir _site
          # Копируем все файлы прототипа
          cp -r prototype/* _site/
          # Копируем ассеты
          cp -r assets _site/
          
          # Исправляем пути к ассетам из "../assets/" на "./assets/",
          # так как на сервере HTML файлы лежат в корне вместе с папкой assets.
          find _site -name "*.html" -type f -exec sed -i 's|\.\./assets/|./assets/|g' {} +
          find _site -name "*.css" -type f -exec sed -i 's|\.\./assets/|./assets/|g' {} +

      - name: Setup Pages
        uses: actions/configure-pages@v4

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: './_site'

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
EOF

echo "✓ Файл .github/workflows/deploy-pages.yml успішно створений."
echo ""
echo "Щоб запустити сайт через GitHub Pages, виконайте наступні кроки:"
echo "1. Додайте створений файл у Git:"
echo "   git add .github/workflows/deploy-pages.yml"
echo "2. Закомітьте зміни:"
echo "   git commit -m \"Додано GitHub Actions для GitHub Pages\""
echo "3. Відправте їх на GitHub:"
echo "   git push origin main"
echo ""
echo "Після цього:"
echo "- Перейдіть у налаштування вашого репозиторію на GitHub (Settings -> Pages)."
echo "- Переконайтеся, що в розділі 'Build and deployment' -> 'Source' вибрано 'GitHub Actions'."
echo "- Деплой почнеться автоматично, і GitHub покаже посилання на ваш сайт!"

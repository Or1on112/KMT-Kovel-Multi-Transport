# Implementation Plan - Joomla 3.10.12 Infrastructure Setup

The goal is to set up a local development environment for Joomla 3.10.12 on Windows without requiring system-wide installations (using portable components).

## Proposed Architecture
- **Web Server/PHP**: PHP 7.4.33 (built-in server).
- **Database**: MariaDB 10.5 Portable.
- **CMS**: Joomla 3.10.12.
- **Location**: All files will be placed in `d:\Projects\KovelPorto\KMT\server`.

## Step-by-Step Task List

### 1. Preparations
- [ ] Create `server` directory.
- [ ] Create subdirectories for `php`, `mariadb`, and `www` (Joomla).

### 2. Download Components
- [ ] Download PHP 7.4.33 (Windows x64).
- [ ] Download MariaDB 10.5 (Windows x64 ZIP).
- [ ] Download Joomla 3.10.12 Full Package.

### 3. Setup MariaDB
- [ ] Extract MariaDB.
- [ ] Initialize the data directory.
- [ ] Create a startup script `start_mysql.bat`.

### 4. Setup PHP
- [ ] Extract PHP.
- [ ] Configure `php.ini` (enable necessary extensions: mysqli, rewrite, etc.).
- [ ] Create a startup script `start_php.bat`.

### 5. Setup Joomla
- [ ] Extract Joomla into `www`.
- [ ] Configure permissions (if needed on Windows).

### 6. Verification
- [ ] Start MariaDB.
- [ ] Start PHP built-in server.
- [ ] Visit the local URL to complete the Joomla installation wizard.

## Risks & Considerations
- **PHP Extensions**: Joomla 3 requires specific extensions (mysqli, gd, curl, openssl, mbstring, xml, zip). I must ensure these are enabled in `php.ini`.
- **Database User**: I will set up a default 'root' user with no password for easier initial setup.
- **Port Conflicts**: Will use default ports (8080 for web, 3306 for DB) unless they are taken.

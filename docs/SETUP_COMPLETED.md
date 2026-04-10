# Joomla! 3.10.12 Infrastructure Setup Summary

The local development environment for Joomla! 3.10.12 has been successfully established. All components are portable and reside within the project directory.

## Environment Details
- **PHP Version**: 7.4.33 (64-bit, Portable)
- **Database**: MariaDB 10.5.23 (64-bit, Portable)
- **CMS**: Joomla! 3.10.12 Stable
- **Local URL**: [http://localhost:8080](http://localhost:8080)
- **Working Directory**: `d:\Projects\KovelPorto\KMT\server`

## Database Connection Info
- **Host**: `localhost`
- **Database Name**: `joomla_db`
- **Username**: `root`
- **Password**: (empty)

## How to Start/Stop the Environment
I have created a helper script to manage the infrastructure:
1. **To Start**: Run the following command in your terminal:
   ```powershell
   powershell.exe -ExecutionPolicy Bypass -File .\run_infrastructure.ps1
   ```
2. **To Stop**: You will need to stop the `php.exe` and `mysqld.exe` processes manually or via Task Manager.

## Next Steps
1. Open [http://localhost:8080/installation/index.php](http://localhost:8080/installation/index.php) in your browser.
2. Follow the Joomla! 3 Web Installer instructions.
3. When prompted for database settings, use the credentials provided above.

> [!TIP]
> After finishing the installation, Joomla! will ask you to delete the `installation` folder for security. You can do this manually or let the installer do it.

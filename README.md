# R2 Storage Cleaner

A Python utility to efficiently clean and manage Cloudflare R2 storage buckets. This tool provides a simple and safe way to delete objects from your R2 storage with detailed progress tracking and error handling.

## Features

- 🚀 Easy-to-use interface for cleaning R2 storage buckets
- 📊 Real-time progress tracking
- ⏱️ Operation timestamps for monitoring
- 🛡️ Error handling and detailed reporting
- 🔄 Pagination support for large buckets
- ⚡ Compatible with Cloudflare R2's S3-compatible API

## Prerequisites

- Python 3.6 or higher
- Cloudflare R2 account with:
  - Account ID
  - Access Key ID
  - Secret Access Key
  - Bucket name

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rkrahulkhorwal/r2-storage-cleaner.git
cd r2-storage-cleaner

Install required dependencies:
bash
pip install boto3
Configuration
Before running the script, you need to set up your R2 credentials. Replace the following values in the script:

Python
ACCOUNT_ID = "your_account_id"
ACCESS_KEY_ID = "your_access_key_id"
SECRET_ACCESS_KEY = "your_secret_access_key"
BUCKET_NAME = "your_bucket_name"
Usage
Run the script with Python:

bash
python r2_cleaner.py
The script will:

Connect to your R2 bucket
List all objects
Delete objects one by one
Provide progress updates
Show a final summary of the operation
Example Output
Code
Starting cleanup of bucket: your-bucket-name
Current UTC time: 2025-01-18 12:30:06
Successfully deleted 10 objects...
Successfully deleted 20 objects...
...
Cleanup Summary:
Successfully deleted: 45 objects
Failed deletions: 0 objects
Operation completed at: 2025-01-18 12:31:15
Safety Considerations
⚠️ Important: Please read before use

Backup: Always ensure you have necessary backups before running cleanup operations
Verification: Double-check your bucket name to avoid accidental deletions
Permissions: Verify your R2 credentials have the required permissions
Testing: Consider testing with a small subset of files first
Error Handling
The script includes comprehensive error handling:

Individual object deletion failures are logged
Overall operation status is reported
Failed deletions are counted and reported separately
Contributing
Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request
License
This project is licensed under the MIT License - see the LICENSE file for details.

Author
rkrahulkhorwal
Acknowledgments
Cloudflare R2 Storage Team
AWS SDK (boto3) developers
Support
If you encounter any issues or have questions, please open an issue on GitHub.

Last updated: 2025-01-18

Code
To complete your GitHub repository, you should also consider adding:

1. A `.gitignore` file:
Python
pycache/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

Virtual Environment
venv/
ENV/

IDE
.idea/
.vscode/
*.swp
*.swo

Operating System
.DS_Store
Thumbs.db

Code
2. A `requirements.txt` file:
boto3>=1.26.0

Code
3. A `LICENSE` file with MIT License:
MIT License

Copyright (c) 2025 rkrahulkhorwal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Code
Would you like me to help you with any specific section of the documentation or create any add

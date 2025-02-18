## FileProbe 📄

🎯 Have URLs in bulks to analyze - specifically, those URL-based file extensions? Seems daunting & inconvenient. Therefore, this program organizes the common file extensions-based URLs, provides their responses, and simple to understand outputs - when providing a URLs-contained file, or a domain.

👀 Suitable for: bug hunters and penetration testers.

# 🚀 Execution Output:
![output](https://github.com/user-attachments/assets/4734deb1-11ca-4aef-a866-b8c5c171cbb2)
# 🏁 Command Flags:

      1. -u: input a single domain for extraction - command: python3 probe.py -u google.com
      2. -f: input a file that contains a list of varying URLs for extract - ensure the file path is wrapped to avoid conflictions - command: python3 probe.py "usr/path/urls-extract/domains.txt"

# ⚙️ Installation:

![carbon-4](https://github.com/user-attachments/assets/6136475f-209f-4007-84a8-884dd1464e7c)

# 🛠️ Features:

      1. File-input that contains URLs
      2. Single domain processing - leveraged automatically with GAU (Get-All-URLs)
      3. Response validation for individual URLs 
      4. Tabulated outputs based on response conditions for organization
      5. Progression bar for monitoring
      6. Termcolor contrast for each phases during execution - clarity

# 👥 Credits:

 - GAU tool: https://github.com/lc/gau (lc/Corben Leo)

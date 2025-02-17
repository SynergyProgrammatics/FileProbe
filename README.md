## FileProbe 📄

🎯 Have URLs in bulks to analyze - specifically, those URL-based file extensions? Seems daunting & inconvenient. Therefore, this program organizes the common file extensions-based URLs,  provides their responses, and simple to understand output. 

👀 Suitable for: bug hunters and penetration testers.

# 🚀 Execution Output:

![output](https://github.com/user-attachments/assets/16ccc513-1771-4d4d-b6e1-a7dd80d93099)

# 🏁 Command Flags:

      1. -u: input a single domain for extraction - command: python3 probe.py -u google.com
      2. -f: input a file that contains a list of varying URLs for extract - ensure the file path is wrapped to avoid conflictions - command: python3 probe.py "domains.txt"

# ⚙️ Installation:

![carbon-3](https://github.com/user-attachments/assets/2d867d1a-da90-41a2-aec2-3d6bb5c66ad7)

# 🛠️ Features:

      1. File-input  - specify path that contains list of URLs to process
      2. Single domain processing - leveraged automatically with GAU (Get-All-URLs)
      3. Response validation for individual URLs 
      4. Tabulated outputs based on response conditions for organization
      5. Progression bar for monitoring
      6. Termcolor contrast for each phases during execution - clarity

# 👥 Credits:

 - GAU tool: https://github.com/lc/gau (lc/Corben Leo)

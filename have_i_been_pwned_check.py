import hashlib
import requests
import sys
import random

from rich import print as printc

def check_haveibeenpwned_db(password: str) -> str:
    """
    This function takes the user's password hash prefix and checks if their password has been compromised 
    using the HaveIBeenPwned database.

    :param password: This is the user's password hash prefix
    """
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    sha1_prefix = sha1_password[:5]
    sha1_suffix = sha1_password[5:]
    with open('db/user_agents.db') as f:
        lines = f.readlines()
        user_agent = random.choice(lines)
    headers = {
        'User-Agent': user_agent[:-1],
        'Referer': "https://haveibeenpwned.com/",
    }

    # Query HIBP's API
    url = f'https://api.pwnedpasswords.com/range/{sha1_prefix}'
    try:
        response = requests.get(url, headers=headers)
    except requests.ConnectionError:
        sys.exit(printc("[red1 b][-] Connection Error:[/red1 b] please retry!"))

    if response.status_code != 200:
        raise RuntimeError(f'Error fetching data: {response.status_code}')

    for line in response.text.splitlines():
        if line.startswith(sha1_suffix):
            count = int(line.split(':')[1])
            if count > 0:
                return f'[red1 b][-] Oh no - pwned! Password found in {count} data breach(es).[/red1 b]'  
    return "[green b][+] Hoorah \o/ - Good news! Password not found in HIBP's data breaches.[/green b]\n[yellow b][!][/yellow b] However, don't overestimate your password strength.\n[deep_pink4 b u]Tip:[/deep_pink4 b u] You should test it using other publicly available databases."
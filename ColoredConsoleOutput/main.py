import colorama
from colorama import Back, Fore, Style

colorama.init(autoreset=True)

print(Fore.RED + "Hello World")
print(Back.GREEN + "Hello World")

print(f"{Fore.RED}H{Fore.YELLOW}E{Fore.GREEN}L{Fore.BLUE}L{Fore.MAGENTA}O")
print(f"{Fore.RED}W{Fore.YELLOW}O{Fore.GREEN}R{Fore.BLUE}L{Fore.MAGENTA}D")


print(f"{Fore.BLACK}{Back.RED}H{Back.YELLOW}E{Back.GREEN}L{Back.BLUE}L{Back.MAGENTA}O")
print(f"{Fore.BLACK}{Back.RED}W{Back.YELLOW}O{Back.GREEN}R{Back.BLUE}L{Back.MAGENTA}D")

print(f"{Fore.RED}{Back.BLACK}{Style.BRIGHT}HELLO WORLD")
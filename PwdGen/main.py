""" PwdGen is a short project to practice Python skills - The purpose of this program is to generate a secure password based on algorithms """

# Import functionality.
from modules.PwdGenerator import PwdGenerator

# Main program function.
def main():
    print(PwdGenerator(lenght=25, security_level=3).generator())

# Main loop.
if __name__ == "__main__":
    main()

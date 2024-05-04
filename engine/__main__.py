from .data import my_resume as context
from .latex import LatexEnvironment


# TODO: Support CLI interface for injecting data and template
def main():
    print(LatexEnvironment().get_template("template.tex").render(**dict(context)))


if __name__ == "__main__":
    main()

import sys
from typing import TextIO

import click
from jinja2 import TemplateError
from pydantic import ValidationError

from engine.models import Resume

from .latex import LatexEnvironment


@click.command()
@click.option(
    "-t",
    "--template",
    "template_file",
    type=click.File("r"),
    help="LaTeX Jinja2 template file used to generate content.",
    required=True,
)
@click.option(
    "-c",
    "--config",
    "config_file",
    type=click.File("r"),
    help="Python module providing a valid `context` object for rendering the given template. If this argument is omitted, config will be read from `stdin` instead.",
    required=False,
)
@click.option(
    "-oe",
    "--omit-email",
    "omit_email",
    type=click.BOOL,
    is_flag=True,
    help="Remove email address from generated resume (if present)",
    default=False,
    show_default=True,
)
@click.option(
    "-op",
    "--omit-phone",
    "omit_phone",
    type=click.BOOL,
    is_flag=True,
    help="Remove phone number from generated resume (if present)",
    default=False,
    show_default=True,
)
def main(
    template_file: TextIO,
    config_file: TextIO | None,
    omit_email: bool,
    omit_phone: bool,
):
    assert template_file

    ### --- Shadow `config_file` from `stdin` if parameter omitted
    if not config_file:
        try:
            config_file = sys.stdin
        except IOError as error:
            print(error)
            return

    ### --- Parse template file
    try:
        template = LatexEnvironment().from_string(template_file.read())
    except Exception as error:
        print(f"Template Parsing: {error}")
        return

    ### --- Parse config file
    resume: Resume | None = None
    try:
        resume = Resume.model_validate_json(config_file.read())

        ### --- Filter out any PII on-demand
        if omit_email:
            resume = resume.without_email()
        if omit_phone:
            resume = resume.without_phone()

    except ValidationError as error:
        print(f"Config Validation: {error}")
        return

    ### --- Render template content
    content: str | None = None
    try:
        content = template.render(**dict(resume))
    except TemplateError as error:
        print(f"Template Rendering: {error}")
        return

    ### --- Output content
    if content:
        sys.stdout.write(content)
        sys.stdout.flush()
    else:
        sys.stderr.write("Unknown error, content object empty")
        sys.stderr.flush()


if __name__ == "__main__":
    main()

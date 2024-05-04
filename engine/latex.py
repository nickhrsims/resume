from os.path import abspath as get_absolute_path

from jinja2 import Environment, FileSystemLoader


class LatexEnvironment(Environment):
    def __init__(self):
        return super().__init__(
            block_start_string=r"\BLOCK{",
            block_end_string=r"}",
            variable_start_string=r"\VAR{",
            variable_end_string=r"}",
            comment_start_string=r"\#{",
            comment_end_string=r"}",
            line_statement_prefix=r"%%",
            line_comment_prefix=r"%#",
            trim_blocks=True,
            autoescape=False,
            loader=FileSystemLoader(get_absolute_path(".")),
        )

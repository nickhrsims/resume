# My Resume Engine

A tiny set of `pydantic` models intended to make writing maintaining my resume easier.

## Why did I make this?

When I first entered college, I truly believed software like LibreOffice and
OpenOffice were the right tool for writing and note taking. As a Linux user,
other office software was off the table anyway, and data ownership feels
important to me. Then, one day while writing a paper, I realize I've spent a
frustrating amount of time fixing broken formatting. It then occurred to me
that I've likely spent more time fixing formatting than working on the paper
content. I discovered LaTeX, and off I went. That was 2018, years and a
pandemic ago. Once I had LaTeX in my hands I realized instantly the power that
I held. "Scripted document generation!", I thought. For the longest time, my
resume existed as a single LaTeX document. Over time, I found that I needed
multiple versions for relevance-related omissions (not all employers care, or
want to necessarily see, all content on my resume). What I really had was a CV
that I wanted to use to generate resumes as sub-sets of content from the whole.
Over time the inter-mingling my resume's content with it's presentation felt
_dirty_. I could explain the technical reasons that it's considered wrong, but
the important thing is that it _felt_ wrong. So, I transpiled my resume's core
content into a `toml` file, and re-wrote the LaTeX template I found online into
a `Jinja2` template. The whole thing was driven by a dirty script that pulled
everything together in a cobbled `venv`. At time of first-publication, I had
reason to make changes yet again. Turns out `toml` isn't so good when the
_structure_ of the content needs to change. It also makes it so that _data
specific_ transformations are either impossible, or with extraneous work in
terms of maintaining schema compatibility: awfully inconvenient. So, I went to
work translating that shoddy `toml` file into a collection of `pydantic`
models; and here we are.

TL;DR: "Why?", said the tree. "For the lulz.", said I.

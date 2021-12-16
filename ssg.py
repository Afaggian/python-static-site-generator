import typer
import ssg.parsers

from ssg.site import Site


def main(source="content", dest="dist", parsers=[ssg.parsers.ResourceParser()]):
    config = {"source": source, "dest": dest, "parsers": parsers}

    Site(**config).build()

typer.run(main)


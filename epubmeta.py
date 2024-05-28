import epub_metadata
import sys
import click


@click.command()
@click.option('--title/--no-title', default=True, help='Output book title')
@click.option('--author/--no-author', default=False,  help='Output book author')
@click.option('--epubfile/--no-epubfile', default=False, help='Output epub file')
def books(title, author, epubfile):
    if title or author:
        for line in sys.stdin:
            line = line.strip()
            if epubfile:
                print(line)
            try:
                metadata = epub_metadata.epub(line).metadata
                if title:
                    print(metadata.title)
                if author:
                    print(metadata.creator)
            except:
                pass
if __name__ == '__main__':
    books()
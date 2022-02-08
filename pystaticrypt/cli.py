"""Console script for pystaticrypt."""

import click
from pystaticrypt.functions import encrypt, decrypt


@click.command()
def main():
    """Main entrypoint."""
    click.echo("pystaticrypt")
    click.echo("=" * len("pystaticrypt"))
    click.echo("Encrypt static html for client-side password access (unsafe for production usage)")
    click.echo("=" * len("pystaticrypt"))
    check()


def check():
    password = "pass"
    contents = "contents"
    s = encrypt(contents, password)
    ds = decrypt(s, password)
    # print(hmac, len(hmac))
    # print(hmac.decode('utf-8'))
    # print(encrypted.encode('utf-8'))
    # s = hmac+encrypted.encode('utf-8')
    print(s)
    print(s[:32])
    print(ds)
    # print(base64.b64encode(hmac))






if __name__ == "__main__":
    main()  # pragma: no cover

import click

@click.group()
def cli():
    pass


@cli.command()
@click.option("--name", prompt="Введіть ім'я", help="Ім'я користувача для виводу")
def say(name):
    if name.lower().startswith('p'):
        click.echo("Ім’я не підходить")
    else:
        click.echo(name)


if __name__ == "__main__":
    cli()

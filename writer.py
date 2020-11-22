from files import *
from paths import *
import click


@click.group()
def writer():
    """- write to file(s)"""
    pass


@writer.command()
@click.argument('name')
def t1(name):
    """- change team 1's name"""
    write(team1F, name)
    click.echo("Team 1 Name: " + read(team1F))


@writer.command()
@click.argument('score')
def t1s(score):
    """- change team 1's score"""
    write(team1scoreF, score)
    click.echo("Team 1 Score: " + read(team1scoreF))


@writer.command()
@click.argument('name')
def t2(name):
    """- change team 2's name"""
    write(team2F, name)
    click.echo("Team 2 Name: " + read(team2F))


@writer.command()
@click.argument('score')
def t2s(score):
    """- change team 2's score"""
    write(team2scoreF, score)
    click.echo("Team 2 Score: " + read(team2scoreF))


@writer.command()
@click.argument('match')
def m(match):
    """- change the match name"""
    write(matchN, match)
    click.echo("Match Name: " + read(matchN))

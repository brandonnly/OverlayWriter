from files import *
from config import *
from rich import print as rprint
import click


@click.group()
def set():
    """- write to file(s)"""
    pass


@set.command()
@click.argument('name', nargs=-1)
def t1(name):
    """- change team 1's name"""
    write(team1F, " ".join(name))
    rprint(f"{main_colour}Team {t1_colour}1 {main_colour}Name: {arg_colour}"
           f"{read(team1F)}")


@set.command()
@click.argument('score')
def t1s(score):
    """- change team 1's score"""
    write(team1scoreF, score)
    rprint(f"{main_colour}Team {t1_colour}1 {main_colour}Score: {arg_colour}"
           f"{read(team1scoreF)}")


@set.command()
@click.argument('name', nargs=-1)
def t2(name):
    """- change team 2's name"""
    write(team2F, " ".join(name))
    rprint(f"{main_colour}Team {t2_colour}2 {main_colour}Name: {arg_colour}"
           f"{read(team2F)}")


@set.command()
@click.argument('score')
def t2s(score):
    """- change team 2's score"""
    write(team2scoreF, score)
    rprint(f"{main_colour}Team {t2_colour}2{main_colour} Score: {arg_colour}"
           f"{read(team2scoreF)}")


@set.command()
@click.argument('match_name', nargs=-1)
def match(match_name):
    """- change the match name"""
    write(matchN, " ".join(match_name))
    rprint(f"{main_colour}Match Name: {arg_colour}{read(matchN)}")


@set.command()
@click.argument('winner_name', nargs=-1)
def winner(winner_name):
    """- change the winner name"""
    write(winnerN, " ".join(winner_name))
    rprint(f"{main_colour}Winner: {arg_colour}{read(winnerN)}")

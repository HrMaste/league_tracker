import configargparse


def track(summoner_id: str, riot_token: str) -> None:
    """Poll Riot API for active games.

    Report game start and end to telegram bot group
    """
    pass


def get_summoner_id(summoner_name: str, riot_token: str) -> str:
    """Use summoner API to get id from a summoner name"""


if __name__ == '__main__':
    parser = configargparse.ArgumentParser()
    parser.add('--riot_token', required=True, env_var='RIOT_TOKEN')
    parser.add('--summoner_name', required=True, env_var='SUMMONER')
    parser.add('--telegram_group_id', required=True, env_var='TELEGRAM_GROUP_ID')
    args = parser.parse_args()
    riot_token = args.riot_token
    summoner_name = args.summoner_name
    summoner_id = get_summoner_id(summoner_name, riot_token)
    track(summoner_id, riot_token)

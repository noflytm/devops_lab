import requests

your_token = {'Authorization': '****past_your_token_here******'}
repo = 'https://api.github.com/repos/alenaPy/devops_lab/pulls'


def get_pulls(state):
    pull = requests.get(repo,
                        headers=your_token)

    if state in ['open', 'closed']:
        pull = requests.get(repo,
                            headers=your_token,
                            params={'state': '{0}'.format(state),
                                    'per_page': '100'})

    if state in ['accepted']:
        pull = requests.get('https://api.github.com/search/issues?q=is:pr%20label:"accepted"\
                   %20repo:alenaPy/devops_lab&per_page=100',
                            headers=your_token,
                            params={'per_page': '100'})
        return pull.json()["items"]

    if state in ['needs work']:
        pull = requests.get('https://api.github.com/search/issues?q=is:pr%20label:"needs%20work"\
                 %20repo:alenaPy/devops_lab&per_page=100', headers=your_token,
                            params={'per_page': '100'})
        return pull.json()["items"]

    return pull.json()

import requests


def get_repo_info(repo_url: str):

    try:
        # Extract repo path
        path = repo_url.replace("https://github.com/", "")

        api_url = f"https://api.github.com/repos/{path}"

        response = requests.get(api_url)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Unable to fetch repo data"}

    except Exception as e:
        return {"error": str(e)}
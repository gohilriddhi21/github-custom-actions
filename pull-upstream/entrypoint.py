import subprocess
import os

def run_command(command, cwd=None):
    """Run a shell command and handle errors."""
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running command: {e}")
        print(f"Error Output: {e.stderr}")

def pull_from_bitbucket_to_github(bitbucket_repo_url, github_repo_path):
    """Pull changes from Bitbucket and push to GitHub."""
    os.chdir(github_repo_path)
    run_command(f'git remote add bitbucket {bitbucket_repo_url}', cwd=github_repo_path)
    run_command('git fetch bitbucket', cwd=github_repo_path)

def main():
    BITBUCKET_REPO = os.environ.get('BITBUCKET_REPO')
    REPO_GITHUB = os.environ.get('REPO_GITHUB')
    branch = 'main' 
    pull_from_bitbucket_to_github(BITBUCKET_REPO, REPO_GITHUB, branch)

if __name__ == '__main__':
    main()
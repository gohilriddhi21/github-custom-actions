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

def pull_from_bitbucket_to_github(bitbucket_repo_url):
    """Pull changes from Bitbucket and push to GitHub."""
    run_command(f'git remote add bitbucket {bitbucket_repo_url}')
    run_command('git fetch bitbucket')

def main():
    BITBUCKET_REPO = os.environ.get('BITBUCKET_REPO')
    pull_from_bitbucket_to_github(BITBUCKET_REPO)

if __name__ == '__main__':
    main()
import os
import sys
import subprocess
import logging
from github import Github
from github import Auth
from genai_model import GenAIModel

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def run_command(command, check=True):
  logger.info(f"Executing command: {command}")
  process = subprocess.Popen(
      command,
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE,
      shell=True,
      universal_newlines=True,
  )
  stdout, stderr = process.communicate()
  logger.debug(f"stdout: {stdout}")
  if check and process.returncode != 0:
      logger.error(f"Command failed with exit code {process.returncode}")
      logger.error(f"Command stderr: {stderr}")
      raise subprocess.CalledProcessError(process.returncode, command, stdout, stderr)
  return stdout.strip()


def get_pull_request_diff():
  """Fetches the Git diff for a given pull request number."""
  current_branch = run_command("git branch --show-current")
  print("\nCurrent Branch: ", current_branch)
  command = "git diff main"
  result = run_command(command)
  return result

      
def send_diff_to_llm(diff):
  client = GenAIModel()
  prompt = "Please provide feedback on the following code changes:\n" + diff
  feedback = client.generate_text(prompt=prompt)
  return feedback


def post_comment(feedback):
    try:
        github_token = os.environ.get("GIT_TOKEN")
        auth = Auth.Token(github_token)
        g = Github(auth=auth)
        logger.info("Connected to github.")
        
        repo_url = os.environ.get("REPO_URL")
        repo = g.get_repo(repo_url)
        logger.info("Repo fetched.")
        
        issue_number = os.environ.get("ISSUE_NUMBER")
        issue = repo.get_issue(number=int(issue_number))
        logger.info("Issue fetched.")
        
        comment_text = f"""
### Successfully generated Feedback!

## GenAI:
{feedback}
        """
        comment = issue.create_comment(comment_text)
        return comment
    except Exception as e:
        logger.error(f"An error occurred while posting comment. {e}")
        raise Exception(e)



def main():
  try:
    run_command("git config --global --add safe.directory /github/workspace")
    
    diff = get_pull_request_diff()
    print(diff)
    
    feedback = send_diff_to_llm(diff)
    print(feedback)
  except Exception as e:
    logger.error(f"An error occurred: {str(e)}")
    sys.exit(1)


if __name__ == "__main__":
    main()
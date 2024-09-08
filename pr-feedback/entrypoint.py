import os
import subprocess
import logging

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


def get_pull_request_diff(pr_number):
  """Fetches the Git diff for a given pull request number."""
  command = "git diff riddhi-dev main"
  result = run_command(command)
  return result


def send_diff_to_llm(diff):
    # TODO: Implement the API call to send the diff to the LLM model
    # Placeholder for feedback generation until you implement the specific API call
    feedback = "**Placeholder:** Feedback will be generated using the LLM model."
    return feedback


def main():
    # PR_TITLE = os.getenv("PR_TITLE")
    ISSUE_NUMBER = os.getenv("ISSUE_NUMBER")
    pr_number = ISSUE_NUMBER  
    diff = get_pull_request_diff(pr_number)
    print("Diff"*10)
    print(diff)
    feedback = send_diff_to_llm(diff)
    print(feedback)


if __name__ == "__main__":
    main()
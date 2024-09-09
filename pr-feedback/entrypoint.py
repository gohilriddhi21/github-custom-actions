import os
import sys
import subprocess
import logging
from vertexai_model import VertexAIModel

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
  PROJECT_ID = os.getenv("PROJECT_ID")
  LOCATION = os.getenv("LOCATION")
  print("PROJECT_ID: ", PROJECT_ID)
  print("LOCATION: ", LOCATION)
  client = VertexAIModel(project=PROJECT_ID, location=LOCATION)
  prompt = "Please provide feedback on the following code changes:\n" + diff
  feedback = client.generate_text(prompt=prompt)
  return feedback


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
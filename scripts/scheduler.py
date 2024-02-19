from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a scheduler
scheduler = BlockingScheduler(timezone='UTC')

# Define the tasks
tasks = [
    r"C:\Users\DELL\Documents\Data Engineering\DataMasters DE Bootcamp\Week 3\Traffic Project\Traffic-ETL\scripts\automated_pipeline.py"
]

# Schedule the tasks
for task in tasks:
    scheduler.add_job(
        lambda: run_task(f'python "{task}"'),
        trigger="cron",
        hour=15,  # Adjust the hour as needed
        minute=50,  # Adjust the minute as needed
        second=0,  # Adjust the second as needed
    )

def run_task(command):
    try:
        logging.info(f"Executing task: {command}")
        subprocess.run(command, shell=True)
        logging.info(f"Task executed successfully.")
    except Exception as e:
        logging.error(f"Error occurred during task execution: {e}")

# Start the scheduler
try:
    logging.info("Scheduler started. Press Ctrl+C to exit.")
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    logging.info("Scheduler stopped.")

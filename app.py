from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import time
from generation_service import generate_answer_gemini
from file_utils import get_first_unanswered_question, replace_question_object_by_id


GEMINI_MODEL = "gemini-2.5-pro"
GEMINI_LIGHT_MODEL = "gemini-2.5-flash"

# Set up the scheduler
scheduler = BackgroundScheduler()

def gemini_generation_job():
    print("Starting GEMINI answer generation job at ", datetime.now())
    question_object = get_first_unanswered_question()
    if (question_object is None):
        print("All questions have been answered. You can stop the job")
        return
    generated_answer = generate_answer_gemini(GEMINI_LIGHT_MODEL, question_object['question'])
    if generated_answer is None:
        print(
            "Answer generation went wrong. Rescheduling job for five minutes from now"
        )
        scheduler.add_job(
            gemini_generation_job,
            trigger="date",
            run_date=datetime.now() + timedelta(minutes=5),
        )
    else:
        print(
            f"Answer correctly generated for question with id: {question_object['id']} "
        )
        question_object['answer'] = generated_answer
        replace_question_object_by_id(question_object['id'], question_object)
        scheduler.add_job(
            gemini_generation_job,
            trigger="date",
            run_date=datetime.now() + timedelta(minutes=30),
        )


scheduler.add_job(gemini_generation_job, trigger="date", run_date=datetime.now())


# Start the scheduler
scheduler.start()

try:
    # Keep the script alive so the scheduler can run
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
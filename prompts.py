RESUME_ANALYSIS_PROMPT = """
You are an expert resume reviewer and ATS optimization assistant.

Analyze this resume and return a clear report with these exact sections:

ATS Score: give one score from 0 to 100.

Professional Summary:
Write a short professional summary.

Key Skills Found:
List skills found in the resume.

Missing or Weak Skills:
List missing or weak skills.

Resume Strengths:
List strengths.

Recommended Improvements:
List specific improvements.

Suggested Resume Bullet Improvements:
Rewrite 3 weak resume bullets into stronger achievement-focused bullets.

Interview Questions:
Create 5 interview questions based on the resume.

Resume:
{resume_text}
"""

JOB_MATCH_PROMPT = """
You are an expert ATS resume matcher.

Compare the resume to the job description and return these exact sections:

Match Score: give one score from 0 to 100.

Best Matching Skills:
List skills from the resume that match the job.

Missing Keywords:
List important keywords from the job description missing from the resume.

Skills Gap:
Explain the biggest gaps.

Resume Changes:
Suggest specific resume changes to improve the match.

Interview Questions:
Create 5 likely interview questions for this job.

Resume:
{resume_text}

Job Description:
{job_description}
"""

COVER_LETTER_PROMPT = """
Write a professional one-page cover letter using the resume and job description.

Resume:
{resume_text}

Job Description:
{job_description}
"""
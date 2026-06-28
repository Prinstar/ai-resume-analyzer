import os
import streamlit as st
from groq import Groq
from prompts import RESUME_ANALYSIS_PROMPT, JOB_MATCH_PROMPT, COVER_LETTER_PROMPT


def get_client():
    api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
    return Groq(api_key=api_key)

def call_groq(prompt):
    client = get_client()

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content


def analyze_resume(resume_text):
    prompt = RESUME_ANALYSIS_PROMPT.format(resume_text=resume_text)
    return call_groq(prompt)


def match_resume_to_job(resume_text, job_description):
    prompt = JOB_MATCH_PROMPT.format(
        resume_text=resume_text,
        job_description=job_description
    )
    return call_groq(prompt)


def generate_cover_letter(resume_text, job_description):
    prompt = COVER_LETTER_PROMPT.format(
        resume_text=resume_text,
        job_description=job_description
    )
    return call_groq(prompt)
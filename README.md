# AI-Powered Mentor Dashboard & Sprint Risk Predictor
A Streamlit-based web application that combines **student/team progress tracking**, **ML-powered sprint risk prediction**, and an **AI mentor chatbot** — all in one dashboard.

## Problem Statement
In academic and agile software environments, mentors and team leads often lack a unified tool to:
- Monitor individual/team performance over time
- Predict early whether a sprint is heading toward failure
- Provide on-demand guidance to students and developers

This project addresses all three using Python, Streamlit, and scikit-learn.

## 🛠️ Tech Stack

**Python 3.10+**

**Streamlit** — UI framework

**scikit-learn** — ML model (Random Forest Classifier)

**pandas / numpy** — Data manipulation

## 📁 Project Structure

```
ai-mentor-dashboard/
├── app.py                  # Main entry point
├── requirements.txt        # Python dependencies
├── README.md               # This file
└── pages/
    ├── __init__.py
    ├── home.py             # Home dashboard page
    ├── tracker.py          # Progress tracker page
    ├── sprint_risk.py      # Sprint risk predictor (ML)
    └── chatbot.py          # AI mentor chatbot
```
## 🤖 ML Model Details

**Model:** Random Forest Classifier (scikit-learn)

**Input Features:**
- Sprint Velocity
- Task Completion Rate
- Number of Active Blockers
- Team Size
- Days Remaining
- Open Bug Count
- Code Reviews Done
- Previous Sprint Risk Flag

**Output:** Binary classification — `At Risk` or `On Track`

**Training Data:** 400 synthetically generated sprint records with realistic risk rules.

**Accuracy:** ~91% on held-out test set

## 💬 AI Mentor Chatbot

The chatbot uses keyword-based response matching and provides suggestions on:
- Study strategies
- Sprint planning
- Team productivity
- ML concepts
- Motivation


## 🧑‍💻 Author
Vedant Deshpande  
BYOP Submission — AI/ML Course  
VIT Bhopal University




